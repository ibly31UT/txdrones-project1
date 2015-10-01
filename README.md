# TXDrones Software Project 1
### DroneConsole

DroneConsole is a webapp written with Python, Flask, Bootstrap and jQuery. It allows any web-enabled device on the same network to access the Raspberry Pi and send commands to the drone. 

The application is divided into two components, the web server and the camera code. Both are run in separate threads. The relevant code for both is in run.py in the main directory. 

For the webserver, run.py references views.py and implicitly \__init__.py (automatically found with the line "from app import app". These set up various routing functions for the webserver to return when a URL is requested. views.py has these routing functions. The actual HTML templates are stored in app/templates and uses __jinja2__ templating engine.

