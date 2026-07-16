import cv2

from src.camera_engine import Camera, CameraManager

manager = CameraManager()

camera = Camera(
    camera_id=1,
    name="Entrance Camera",
    source="assets/sample.mp4"
)

manager.add_camera(camera)

camera.connect()

while True:

    frame = camera.read()

    if frame is None:
        break

    cv2.imshow(camera.name, frame)

    if cv2.waitKey(1) == ord("q"):
        break

camera.disconnect()

cv2.destroyAllWindows()