import cv2
from PIL import Image, ImageChops
import time

x=1
while x == 1:
    time.sleep(300)
    camera_port = 1
    ramp_frames = 30

    camera = cv2.VideoCapture(camera_port)

    def get_image():
        retval, im = camera.read()
        return im

    for i in range(ramp_frames):
        temp = get_image()

    print("Checking Posture")

    camera_capture = get_image()
    file = "Basic.png"
    cv2.imwrite(file, camera_capture)

    del camera
    print("Posture Checked")

    img2 = Image.open('Basic.png')
    img1 = Image.open('Source.png')

    diff = ImageChops.difference(img1,img2)

    if diff.getbbox():
        diff.show()
        diff.save("ChangePosture.png")
