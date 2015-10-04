from app import app
from threading import Thread
import time
from datetime import datetime
import picamera
from picamera.array import PiRGBArray
import cv2

class VideoThread(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.camera = picamera.PiCamera()
		self.camera.vflip = True
		self.camera.framerate = 30
		self.camera.resolution = (640, 480)
		self.camera.use_video_port = True
		self.camera.quality = 85

		self.rawCapture = PiRGBArray(self.camera, size=(640, 480))

	def run(self):
		time.sleep(1) # warm up the camera

		for frame in camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
			image = frame.array

			cv2.imshow("Frame", image)
			key = cv2.waitKey(1) & 0xFF

			self.rawCapture.truncate(0)

			if key == ord("q"):
				break

class ServerThread(Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		app.run(host='0.0.0.0', threaded=True)


if __name__ == "__main__":
	print "Running __main__ again"	
	VideoThread().start()
	#ServerThread().start()
