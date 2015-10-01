from app import app
from threading import Thread
import time
from datetime import datetime
import picamera
import picamera.array
import io

class VideoThread(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.camera = picamera.PiCamera()
		self.camera.vflip = True
		self.camera.framerate = 30
		self.camera.resolution = (1280, 720)
		self.camera.use_video_port = True
		self.camera.quality = 85

	def run(self):
		self.camera.start_preview()
		time.sleep(2)

		i = 0
		while True:
			#self.camera.capture("app/frame%d.jpeg" % i)	
			print "Capture %d at %s\n" % ( i, str(datetime.now()) )
			i += 1
			time.sleep(0.01)
		
		self.camera.stop_preview()	 

class ServerThread(Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		app.run(host='0.0.0.0', threaded=True)


if __name__ == "__main__":
	print "Running __main__ again"	
	VideoThread().start()
	#ServerThread().start()
