from flask import render_template
from app import app

navigation = [{"name": "Home", "link": "index"}, {"name": "GPS Map", "link": "gps"}, {"name": "Live Video Feed", "link": "video"}]

@app.route("/")
@app.route("/index")
def index():
	buttons = navigation
	return render_template("index.html", title="Home", buttons=buttons, navigation=navigation)

@app.route("/gps")
def gps():
	user = "Will"
	return render_template("gps.html", title="GPS Map", user=user, navigation=navigation)

@app.route("/video")
def video():
	return render_template("video.html", title="Live Video Feed", navigation=navigation)

# As of now this video_frame_generator multipart system is not working. Working on implementing an ajax solution to this problem

frame_count = 0
def video_frame_generator():
	print "getting a frame"
	while(True):
		print "Yielding frame %d" % frame_count
		frame = open("app/frame%d.jpeg" % frame_count, "rb").read()
		
		frame_count += 1
		yield (	b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route("/video_feed")
def video_feed():
	return Response(video_frame_generator(), mimetype="multipart/x-mixed-replace; boundary=frame")
