from time import sleep 
from picamera import PiCamera

camera = PiCamera()
sleep(1)
camera.capture("/home/pi/Pictures/img.png")
print("Done.")