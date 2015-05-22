import sys
import time
import numpy
from PIL import Image

from naoqi import ALProxy

def get_image_from_camera(IP, PORT):
    camProxy = ALProxy("ALVideoDevice", IP, PORT)
    resolution = 2    # VGA
    colorSpace = 11   # RGB

    videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)


    # Get a camera image.
    # image[6] contains the image data passed as an array of ASCII chars.
    naoImage = camProxy.getImageRemote(videoClient)




    camProxy.unsubscribe(videoClient)


    # Get the image size and pixel array.
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]

    # Create a PIL Image from our pixel array.
    im = Image.fromstring("RGB", (imageWidth, imageHeight), array)

    # Save the image.
    #im.save("camImage.png", "PNG")
    #im.show()


    # via http://stackoverflow.com/questions/14134892/convert-image-from-pil-to-opencv-format
    open_cv_image = numpy.array(im)
    # Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    return open_cv_image
