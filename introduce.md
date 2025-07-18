# 行人检测追踪与双向流量计数系统

## 一、项目简介

本项目基于 Ultralytics YOLO 模型（yolo11m）与 PySide6 框架，提供一个简洁易用的图形化界面，可用于实时视频/摄像头的目标检测、跟踪与统计展示。主要功能包括：

- 支持本地视频文件（mp4/avi/mov/mkv）和摄像头实时流输入
- 基于 YOLO 模型进行检测，并使用持续跟踪策略分配唯一 ID
- 可选显示检测框、目标 ID 标签和运动轨迹
- 统计每帧目标上下移动次数并实时更新
- 下方信息表格展示当前帧所有检测目标的序号、ID、置信度、类别及坐标
- 右侧面板显示总目标数、实时 FPS 与运行时长
- 提供置信度阈值调节器与显示选项切换复选框

## 二、环境依赖

- Python 3.8+
- ultralytics >= 8.x（YOLO 模型加载与跟踪）
- opencv-python
- numpy
- PySide6

安装示例：

```bash
pip install ultralytics opencv-python numpy PySide6
```

## 三、代码结构

```text
project_root/
├─ main.py           # 主程序入口，包含 MainWindow 类
├─ per.py            # Qt Designer 转换生成的 UI 模块
├─ yolo11m.pt        # YOLO 模型权重文件
└─ README.md         # 本说明文档
```

## 四、主要模块说明

### 1. MainWindow 类

![image-20250718140719350](C:\Users\zero\AppData\Roaming\Typora\typora-user-images\image-20250718140719350.png)

![image-20250718140807830](C:\Users\zero\AppData\Roaming\Typora\typora-user-images\image-20250718140807830.png)

负责加载 UI、初始化模型与控件、管理视频流、处理定时器回调，实现检测、跟踪及可视化展示。其核心方法如下：

- `__init__()`
  - 加载 `per.Ui_MainWindow`
  - 嵌入 `QLabel` 用于视频显示
  - 配置下方 `QTableWidget` 显示检测信息
  - 初始化 YOLO 模型与跟踪历史容器
  - 将置信度控制与复选框、按钮信号连接
  - 启动 `QTimer`，每秒 30 帧调用 `update_frame()`
- `open_camera()`
  - 切换摄像头流（打开/关闭）
  - 打开时重置计数、ID 历史、显示按钮文字
- `open_video()`
  - 弹出文件对话框选择视频
  - 切换视频流状态，参数与摄像头类似
- `update_frame()`
  1. 计算并更新实时 FPS
  2. 读取一帧并调用 `model.track()` 进行目标检测与跟踪
  3. 根据置信度阈值过滤结果
  4. 清理已消失（Track 断开）的目标历史
  5. 将图像缩放以适配界面
  6. 统计每帧目标的上下移动（正/反向计数）
  7. 可选绘制检测框与 ID 标签
  8. 更新运动轨迹并可选显示
  9. 将最终图像渲染到 `QLabel`
  10. 更新下方表格与右侧统计信息

### 2. per.py

由 Qt Designer 生成，定义窗口布局和各控件（按钮、复选框、表格、标签等），通过 `setupUi(self)` 完成界面初始化。



## 五、运行与使用说明

1. 确保已安装环境依赖，且 `yolo11m.pt` 权重文件位于项目目录

2. 在终端运行：

   ```bash
   python main.py
   ```

3. 点击“打开视频”按钮选择本地视频，或点击“打开摄像头”启动实时流

4. 通过界面右侧复选框切换是否显示检测框、运动轨迹

5. 使用下方置信度 `doubleSpinBox` 调整检测灵敏度

6. 实时查看下方表格与右侧数值统计

## 六、参数配置

| 参数名               | 说明                   | 默认值  |
| -------------------- | ---------------------- | ------- |
| `model.conf`         | YOLO 检测置信度阈值    | 0.25    |
| `QTimer` 频率        | 帧率控制（毫秒）       | 1000/30 |
| `track_history` 大小 | 运动轨迹保存的最大帧数 | 30      |

## 七、注意事项与拓展

- 确保摄像头设备正常接入，否则 `cv2.VideoCapture(0)` 无法打开
- 若需要其他类别检测，可调整 `classes=[0]` 中的索引或开放其他类
- 运动轨迹最大长度可根据需求在 `track_history` 中修改
- 可结合 SQLite、CSV 等方式将检测结果持久化存储

