class CameraManager:

    def __init__(self):
        self.cameras = {}

    def add_camera(self, camera):
        self.cameras[camera.camera_id] = camera

    def get_camera(self, camera_id):
        return self.cameras.get(camera_id)

    def remove_camera(self, camera_id):
        if camera_id in self.cameras:
            self.cameras[camera_id].disconnect()
            del self.cameras[camera_id]