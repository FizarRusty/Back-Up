import picamera


camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = (30)
camera.start_recording('output.h264')
camera.wait_recording(3)
camera.stop_recording()
