import cv2
import numpy as np
import time
import PoseModule as pm

detector = pm.poseDetector()
cap = cv2.VideoCapture(0)

count = 0
dir = 0

while True:
        # Image
        # img = cv2.imread("Sources/roro1.jpg")

        # Video
        _, img = cap.read()
        img = cv2.resize(img, (1280, 720))

        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)
        # print(lmList)
        if len(lmList) != 0:
                #Right Arm (more infos on mediapipe documentation)
                angle = detector.findAngle(img, 12, 14, 16)
                # #Left Arm
                # detector.findAngle(img, 11, 13, 15)
                per = np.interp(-angle, (-130, -60), (0, 100))
                bar = np.interp(-angle, (-130, -60), (650, 100))

                color = (255, 0, 255)
                if per == 100:
                        color = (0, 255, 0)
                        if dir == 0:
                                count += 0.5
                                dir = 1
                if per == 0:
                        color = (0, 255, 0)
                        if dir == 1:
                                count += 0.5
                                dir = 0
                # print(count)

                cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
                cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
                cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                            color, 4)

                cv2.rectangle(img, (0, 550), (250, 720), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(count)), (45, 690), cv2.FONT_HERSHEY_PLAIN, 8,
                            (255, 0, 0), 15)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
