import cv2

from src.common import Frame

image = cv2.imread("assets/sample.jpeg")

frame = Frame(
    frame_id=1,
    camera_id=101,
    image=image,
)

print(frame.frame_id)
print(frame.camera_id)
print(frame.timestamp)
print(frame.image.shape)