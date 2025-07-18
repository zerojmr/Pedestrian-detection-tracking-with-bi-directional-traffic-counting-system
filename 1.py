from collections import defaultdict
import cv2
import numpy as np
from ultralytics import YOLO

# —— 1. 加载模型 ——  
model = YOLO("yolo11m.pt")
model.conf = 0.25

# —— 2. 打开视频 ——  
video_path = "per.mp4"
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("❌ 无法打开视频源")
    exit()

# —— 3. 存储每个 track_id 的历史中心点 ——  
track_history = defaultdict(list)

# —— 4. 设定显示宽度 ——  
DISPLAY_W = 640

# —— 5. 循环处理每帧 ——  
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # —— 5.1 检测＋跟踪 ——  
    res = model.track(frame, persist=True, classes=[0])[0]

    # —— 5.2 获取已画框+ID 的 RGB 图，并转 BGR ——  
    vis = res.plot()  
    vis = cv2.cvtColor(vis, cv2.COLOR_RGB2BGR)

    # —— 5.3 更新轨迹中心点 ——  
    if res.boxes.id is not None:
        xywh      = res.boxes.xywh.cpu().numpy()       # (N,4)
        track_ids = res.boxes.id.cpu().numpy().astype(int)
        for (x, y, w, h), tid in zip(xywh, track_ids):
            pts = track_history[tid]
            pts.append((int(x), int(y)))
            if len(pts) > 30:
                pts.pop(0)

    # —— 5.4 绘制轨迹线 ——  
    for pts in track_history.values():
        if len(pts) > 1:
            arr = np.array(pts, dtype=np.int32).reshape(-1,1,2)
            cv2.polylines(vis, [arr], False, (0,255,0), 2)

    # —— 5.5 按比例缩放 ——  
    h, w = vis.shape[:2]
    new_h = int(h * (DISPLAY_W / w))
    small = cv2.resize(vis, (DISPLAY_W, new_h))

    # —— 5.6 显示 ——  
    cv2.imshow("YOLO11 Tracking (缩小预览)", small)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
