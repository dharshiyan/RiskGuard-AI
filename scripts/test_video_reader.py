import cv2

from src.video_engine import VideoReader

VIDEO_PATH = "assets/sample.mp4"

reader = VideoReader(VIDEO_PATH)

reader.open()

while True:
    frame = reader.read()

    if frame is None:
        break

    cv2.imshow("Video Engine", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

reader.release()
cv2.destroyAllWindows()