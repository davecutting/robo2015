import io
import picamera
import cv2
import time
import numpy as np
import serial
from PIL import Image
import picamera.array
camheight=180
camwidth=320
radius = 5
#ser = serial.Serial('/dev/ttyACM0', 57600)
camera=picamera.PiCamera()
camera.resolution = (camwidth,camheight)
stream = io.BytesIO()
#camera.start_recording(stream_video, format='h264', quality=23)
print time.clock()
while True:
    #print time.clock()
    #saving the picture to an in-program stream rather than a file
    stream.seek(0)
    camera.capture(stream, 'jpeg', use_video_port = True)
    #with picamera.array.PiRGBArray(camera) as stream:
        #camera.capture(stream, format = 'bgr', use_video_port = True)
        #data = stream.array
        #print time.clock()
    
    #capture into stream
    #camera.capture(stream, format='jpeg')
    #convert image into numpy array
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    #print time.clock()
    image = cv2.imdecode(data, 1)
    #cv2.imshow("Image",image)
    #cv2.waitKey(0)
    #orig = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Greyscale", gray)
    # apply a Gaussian blur to the image then find the brightest
    # region
    #gray = image[:,:,2]
    #gray = cv2.GaussianBlur(image, (radius, radius), 0)
    #print time.clock()
    #plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
    #plt.show()
    gray = cv2.boxFilter(gray, -1, (radius, radius))
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    #plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
    #plt.show()
    #print time.clock()
    #print time.clock()
    Coord = (camwidth/2, 0.8*camheight)
    distance_from_obj_tup=(maxLoc[0]-Coord[0],-1*(maxLoc[1]-Coord[1]))
    #print distance_from_obj_tup    
    #color = image[maxLoc[0], maxLoc[1]]
    #colorvalred = color[0]
    # x_coord=distance_from_obj_tup[0]
    # y_coord=distance_from_obj_tup[1]
    # print x_coord, y_coord
    # display the results of our newly improved method
    # cv2.imshow("Robust", image)
    # cv2.waitKey(0)
    if maxVal < 50 :
        #cv2.imshow("Image",data)
        #cv2.waitKey(0)
        distance_from_obj_tup = (0,0)
        #ser.write("("+str(distance_from_obj_tup[0])+", "+str(distance_from_obj_tup[1])+")")
    #print time.clock()
    # turn the array into a cv2 image
    #cv2.imshow("Image",resized)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #print time.clock()
    print distance_from_obj_tup
    #cv2.imshow("Image",image)
    #cv2.waitKey(0)
print time.clock()
