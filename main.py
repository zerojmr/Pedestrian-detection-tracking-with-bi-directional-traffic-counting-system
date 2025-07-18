# -*- coding: utf-8 -*-
import sys
import time
from collections import defaultdict

import cv2
import numpy as np
from ultralytics import YOLO
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QFileDialog, QLabel, QHBoxLayout

from per import Ui_MainWindow  # UI界面文件，由pyside6-uic工具生成

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # 1. 加载UI界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 用于实时FPS计算的时间记录
        self.prev_time = None

        # 用于跟踪物体运动方向的状态变量
        self.id_state = {}  # 物体ID状态记录
        self.last_y = {}    # 记录每个ID上一帧的Y坐标
        self.forward_count = 0  # 正向运动计数
        self.backward_count = 0  # 反向运动计数

        # —— 在videoWidget中嵌入QLabel用于显示视频 —— #
        self.video_label = QLabel(self.ui.videoWidget)
        self.video_label.setObjectName("videoLabel")
        self.video_label.setAlignment(QtCore.Qt.AlignCenter)
        # 设置尺寸策略为可扩展
        self.video_label.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        self.video_label.setScaledContents(True)  # 缩放内容以适应标签大小
        # 创建布局并添加视频标签
        video_layout = QHBoxLayout(self.ui.videoWidget)
        video_layout.setContentsMargins(0, 0, 0, 0)
        video_layout.addWidget(self.video_label)

        # —— 初始化底部信息表格 —— #
        self.ui.inf_tableWidget.setColumnCount(5)  # 5列
        self.ui.inf_tableWidget.setHorizontalHeaderLabels(
            ["序号", "ID", "置信度", "类型", "坐标"]  # 列标题
        )
        # 设置列自动拉伸
        self.ui.inf_tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )

        # 初始化复选框状态
        self.show_trajectory = self.ui.guiji_checkBox.isChecked()  # 是否显示轨迹
        self.show_labels = self.ui.text_checkBox.isChecked()  # 是否显示标签
        # 连接复选框信号
        self.ui.guiji_checkBox.toggled.connect(lambda b: setattr(self, 'show_trajectory', b))
        self.ui.text_checkBox.toggled.connect(lambda b: setattr(self, 'show_labels', b))

        # 2. 连接按钮信号
        self.ui.vedio_pushButton.clicked.connect(self.open_video)  # 打开视频按钮
        self.ui.camera_pushButton.clicked.connect(self.open_camera)  # 打开摄像头按钮

        # 3. 初始化成员变量
        self.cap = None  # 视频捕获对象
        self.start_time = None  # 开始时间记录
        self.frame_count = 0  # 帧计数器
        self.current_source = ""  # 当前视频源（文件路径或"摄像头"）

        # 4. 加载YOLO+跟踪模型
        self.model = YOLO("yolo11m.pt")  # 加载预训练模型
        self.model.conf = 0.25  # 默认置信度阈值
        self.track_history = defaultdict(list)  # 跟踪历史记录

        # —— 配置置信度调节控件 —— #
        self.ui.doubleSpinBox.setRange(0.0, 1.0)  # 设置范围0-1
        self.ui.doubleSpinBox.setSingleStep(0.01)  # 步长0.01
        self.ui.doubleSpinBox.setDecimals(2)  # 小数点后2位
        self.ui.doubleSpinBox.setValue(self.model.conf)  # 设置初始值
        # 连接值改变信号
        self.ui.doubleSpinBox.valueChanged.connect(lambda v: setattr(self.model, 'conf', v))

        # 5. 定时器：30FPS采集+刷新
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)  # 连接定时器信号
        self.timer.start(int(1000 / 30))  # 约33ms一帧

    def open_camera(self):
        """切换摄像头流：打开或关闭本机摄像头"""
        # 如果摄像头已打开，则关闭
        if self.cap and self.cap.isOpened():
            self.cap.release()
            self.cap = None
            self.ui.camera_pushButton.setText("打开摄像头")
            self.video_label.clear()  # 清空显示
            return

        # 尝试打开本机摄像头(0号设备)
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            QtWidgets.QMessageBox.warning(self, "错误", "无法打开摄像头")
            self.cap = None
            return

        # 重置计数器和状态
        self.forward_count = 0
        self.backward_count = 0
        self.last_y.clear()  # 清空Y坐标记录
        self.ui.forward_label.setText("0")  # 重置显示
        self.ui.backward_label.setText("0")

        # 重置其他状态
        self.start_time = time.time()  # 记录开始时间
        self.frame_count = 0  # 重置帧计数器
        self.track_history.clear()  # 清空跟踪历史
        self.current_source = "摄像头"  # 设置当前源
        self.ui.camera_pushButton.setText("关闭摄像头")  # 更新按钮文本
        self.prev_time = time.time()  # 重置FPS计算时间

    def open_video(self):
        """切换视频流：打开或关闭用户选中的视频"""
        # 如果视频已打开，则关闭
        if self.cap and self.cap.isOpened():
            self.cap.release()
            self.cap = None
            self.ui.vedio_pushButton.setText("打开视频")
            self.video_label.clear()  # 清空显示
            return

        # 弹出文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择视频文件",
            "",  # 默认目录
            "视频文件 (*.mp4 *.avi *.mov *.mkv);;所有文件 (*)"  # 文件过滤器
        )
        if not file_path:  # 用户取消选择
            return

        # 尝试打开视频文件
        self.cap = cv2.VideoCapture(file_path)
        if not self.cap.isOpened():
            QtWidgets.QMessageBox.warning(self, "错误", "无法打开视频文件")
            self.cap = None
            return

        # 重置计数器和状态
        self.forward_count = 0
        self.backward_count = 0
        self.last_y.clear()
        self.ui.forward_label.setText("0")
        self.ui.backward_label.setText("0")

        # 重置其他状态
        self.start_time = time.time()
        self.frame_count = 0
        self.track_history.clear()
        self.current_source = file_path  # 记录当前视频路径
        self.ui.vedio_pushButton.setText("关闭视频")  # 更新按钮文本
        self.prev_time = time.time()

    def update_frame(self):
        """定时器槽函数：更新视频帧并进行处理"""
        frame_forward = 0  # 本帧正向运动计数
        frame_backward = 0  # 本帧反向运动计数
        
        # —— 1. 计算实时FPS —— #
        curr_time = time.time()
        # 计算当前FPS（帧间隔时间的倒数）
        real_fps = 0.0 if self.prev_time is None else 1.0 / (curr_time - self.prev_time)
        self.prev_time = curr_time

        # 如果没有视频源或未打开，直接返回
        if not self.cap or not self.cap.isOpened():
            return

        # 读取视频帧
        ret, frame = self.cap.read()
        if not ret:  # 读取失败
            return

        self.frame_count += 1  # 帧计数器递增

        # —— 2. 使用YOLO进行检测+跟踪 —— #
        # 只检测人(classes=[0])，并保持跟踪状态(persist=True)
        res = self.model.track(frame, persist=True, classes=[0])[0]

        # —— 3. 提取结果并过滤置信度 —— #
        if res.boxes.id is not None:  # 如果有检测结果
            # 获取边界框坐标(xyxy格式)
            xyxy = res.boxes.xyxy.cpu().numpy().astype(int)
            # 获取边界框中心坐标和宽高(xywh格式)
            xywh = res.boxes.xywh.cpu().numpy()
            # 获取跟踪ID
            tids = res.boxes.id.cpu().numpy().astype(int)
            # 获取置信度
            confs = res.boxes.conf.cpu().numpy()
        else:  # 没有检测结果时创建空数组
            xyxy = np.zeros((0, 4), int)
            xywh = np.zeros((0, 4))
            tids = np.zeros((0,), int)
            confs = np.zeros((0,), float)

        # 根据置信度阈值过滤结果
        mask = confs >= self.model.conf
        xyxy, xywh, tids, confs = xyxy[mask], xywh[mask], tids[mask], confs[mask]

        # —— 4. 清理过期轨迹 —— #
        current_ids = set(tids.tolist())  # 当前帧中的所有ID
        # 删除不再存在的ID的轨迹历史
        for tid in list(self.track_history):
            if tid not in current_ids:
                del self.track_history[tid]

        # —— 5. 缩放帧以适应显示区域 —— #
        vis = frame.copy()  # 创建帧副本用于可视化
        dw = self.ui.videoWidget.width()  # 获取显示区域宽度
        h0, w0 = vis.shape[:2]  # 原始帧高度和宽度
        # 计算新高度以保持宽高比
        new_h = int(h0 * (dw / w0))
        # 缩放帧
        vis_small = cv2.resize(vis, (dw, new_h))
        # 计算缩放比例(用于后续坐标转换)
        scale_x = dw / w0
        scale_y = new_h / h0

        # —— 6. 基于Y坐标变化统计正/反向运动 —— #
        for (_, cy, _, _), tid in zip(xywh, tids):
            prev_y = self.last_y.get(tid)  # 获取上一帧的Y坐标
            curr_y = cy  # 当前Y坐标
            if prev_y is not None:  # 如果有上一帧数据
                dy = curr_y - prev_y  # 计算Y坐标变化
                if dy > 0:  # 向下移动(正向)
                    frame_forward += 1
                elif dy < 0:  # 向上移动(反向)
                    frame_backward += 1
            # 更新last_y供下一帧比较
            self.last_y[tid] = curr_y
        
        # 更新UI显示
        self.ui.forward_label.setText(str(frame_forward))
        self.ui.backward_label.setText(str(frame_backward))

        # —— 8. 绘制检测框和ID标签 —— #
        if self.show_labels:  # 如果勾选了显示标签
            for (x1, y1, x2, y2), tid in zip(xyxy, tids):
                # 转换坐标到缩放后的帧
                x1s, y1s = int(x1 * scale_x), int(y1 * scale_y)
                x2s, y2s = int(x2 * scale_x), int(y2 * scale_y)
                # 绘制红色矩形框
                cv2.rectangle(vis_small, (x1s, y1s), (x2s, y2s), (0, 0, 255), 3)
                # 在框上方显示ID
                cv2.putText(vis_small, f"ID:{tid}", (x1s, y1s - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # —— 9. 更新并绘制轨迹 —— #
        for (x, y, _, _), tid in zip(xywh, tids):
            pts = self.track_history[tid]  # 获取该ID的轨迹点
            pts.append((int(x), int(y)))  # 添加新点
            if len(pts) > 30:  # 限制轨迹长度
                pts.pop(0)
        
        if self.show_trajectory:  # 如果勾选了显示轨迹
            for pts in self.track_history.values():
                if len(pts) > 1:  # 至少有2个点才能画线
                    # 转换坐标到缩放后的帧
                    pts_s = [(int(x * scale_x), int(y * scale_y)) for x, y in pts]
                    # 转换为numpy数组并绘制绿色轨迹线
                    arr = np.array(pts_s, dtype=np.int32).reshape(-1, 1, 2)
                    cv2.polylines(vis_small, [arr], False, (0, 255, 0), 2)

        # —— 10. 显示处理后的帧到QLabel —— #
        h1, w1, c1 = vis_small.shape
        # 将OpenCV图像转换为Qt图像格式
        qimg = QtGui.QImage(vis_small.data, w1, h1, c1 * w1, QtGui.QImage.Format_BGR888)
        # 设置到QLabel显示
        self.video_label.setPixmap(QtGui.QPixmap.fromImage(qimg))

        # —— 11. 更新信息表格 —— #
        cnt = len(tids)  # 检测到的物体数量
        self.ui.inf_tableWidget.setRowCount(cnt)  # 设置行数
        for i in range(cnt):
            x1, y1, x2, y2 = xyxy[i]
            # 创建表格项
            items = [
                QtWidgets.QTableWidgetItem(str(i + 1)),  # 序号
                QtWidgets.QTableWidgetItem(str(tids[i])),  # ID
                QtWidgets.QTableWidgetItem(f"{confs[i]:.2f}"),  # 置信度(保留2位小数)
                QtWidgets.QTableWidgetItem("person"),  # 类型(固定为人)
                QtWidgets.QTableWidgetItem(f"{x1},{y1},{x2},{y2}"),  # 坐标
            ]
            # 设置文本居中并添加到表格
            for col, it in enumerate(items):
                it.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.inf_tableWidget.setItem(i, col, it)

        # —— 12. 更新右侧统计信息 —— #
        self.ui.number_label.setText(str(len(self.track_history)))  # 当前跟踪的物体数量
        self.ui.lblFPS_label.setText(f"{real_fps:.1f}")  # 显示FPS(保留1位小数)
        elapsed = time.time() - self.start_time  # 计算运行时间
        m, s = divmod(elapsed, 60)  # 转换为分钟和秒
        self.ui.lblElapsedTime_label.setText(f"{int(m)}分{s:.1f}秒")  # 显示运行时间


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())