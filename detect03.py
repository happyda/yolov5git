# detect03.py
import numpy as np
import cv2
import torch.hub
import time
import pafy


model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp5/weights/best.pt',force_reload=True)
# url = "https://www.youtube.com/watch?v=wo-78u7P6Fk&t=7s"
# url = "https://www.youtube.com/watch?v=CmWBk-27B3g"
# live = pafy.new(url)
# stream = live.getbest(preftype="mp4")
# cap = cv2.VideoCapture("https://cctvn.freeway.gov.tw/abs2mjpg/bmjpg?camera=13380")
# cap = cv2.VideoCapture("https://cctv.klcg.gov.tw/facd4662")
# cap = cv2.VideoCapture("https://cctv7.kctmc.nat.gov.tw/play/live.php?devid={79d8a119-9164-1f84-a1c8-da4f5fb99508}&L=dfe8885c1acbe4c5e5fb91e6d9bd3724")
# cap = cv2.VideoCapture("https://cctv1.kctmc.nat.gov.tw/f75bb280?t=0.9768836315531848")
# cap = cv2.VideoCapture(stream.url)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ingnoring empty camera frame.")
        continue
    frame = cv2.resize(frame,(800,480))
    # frame = cv2.flip(frame,1)
    results = model(frame)
    cv2.imshow('YOLO COCO 01 M11008910', np.squeeze(results.render()))
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cav.destoryAllWindows()
