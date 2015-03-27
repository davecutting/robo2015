import io
import picamera
import cv2
import time
import numpy as np
import serial
from PIL import Image
camheight=180
camwidth=320
radius = 5
ser = serial.Serial('/dev/ttyACM0', 57600)
camera=picamera.PiCamera()
camera.resolution = (camwidth,camheight)
stream = io.BytesIO()
#camera.start_recording(stream_video, format='h264', quality=23)
#print time.clock()
for x in range(11):
    #saving the picture to an in-program stream rather than a file
    stream.seek(0)
    camera.capture(stream, 'jpeg', use_video_port = True)
    #print time.clock()
    
    #capture into stream
    #camera.capture(stream, format='jpeg')
    #convert image into numpy array
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    image = cv2.imdecode(data, 0)
    #orig = image.copy()
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # apply a Gaussian blur to the image then find the brightest
    # region
    #gray = image[:,:,2]
    gray = cv2.GaussianBlur(image, (radius, radius), 0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    #print time.clock()
    Coord = (camwidth/2, 0.8*camheight)
    #color = orig[maxLoc[0], maxLoc[1]]
    #colorvalred = color[0]
    distance_from_obj_tup=(maxLoc[0]-Coord[0],-1*(maxLoc[1]-Coord[1]))
        
    print distance_from_obj_tup
        
    # x_coord=distance_from_obj_tup[0]
    # y_coord=distance_from_obj_tup[1]
    # print x_coord, y_coord
    # display the results of our newly improved method
    # cv2.imshow("Robust", image)
    # cv2.waitKey(0)
    if True:#colorvalred > 10 :
        ser.write("("+str(distance_from_obj_tup[0])+", "+str(distance_from_obj_tup[1])+")")
    #print time.clock()
    # turn the array into a cv2 image
    #cv2.imshow("Image",resized)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
