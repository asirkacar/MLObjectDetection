import os
import time
import uuid
import cv2

labels = [{'name':'Mask', 'id':1}, {'name':'NoMask', 'id':2}]

IMAGE_PATH = 'Tensorflow/workspace/images/collectedimages'

labels = ['Hello', 'thanks', 'yes', 'no', 'i love you']
number_imgs = 15

for label in labels:
    directory = label

    parent_dir = "Tensorflow/workspace/images/collectedimages"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

    #os.mkdir('Tensorflow\workspace\images\collectedimages\\'+label)
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}' .format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGE_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
