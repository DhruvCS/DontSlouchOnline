import cv2

#this number may need to be changed to fit your needs
camera_port = 1
ramp_frames = 30

camera = cv2.VideoCapture(camera_port)

def get_image():
    retval, im = camera.read()
    return im

for i in range(ramp_frames):
    temp = get_image()

print("Taking Picture")

camera_capture = get_image()
file = "Source.png"
cv2.imwrite(file, camera_capture)

del camera
print("Picture Taken")
