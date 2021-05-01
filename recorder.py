import cv2
from os import system
from datetime import datetime
import notifier
import database_access


def recorder():
    cam = cv2.VideoCapture(2)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    filename = f"{datetime.now().date()}-{datetime.now().time()}-output.avi"
    path = ".Video-Files/"
    size = (int(cam.get(3)), int(cam.get(4)))
    output = cv2.VideoWriter(filename, fourcc, 60, size)

    while cam.isOpened():
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1, frame2)
        grey = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(grey, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=5)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
        for c in contours:
            if cv2.contourArea(c) < 5000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            flag = True
            if flag:
                notifier.desktop_notify("Alert!", "Movement detected, may be a burglar")
                # notifier.mobile_notify("Alert!", "Movement detected, may be a burglar")
                flag = False

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        output.write(frame1)
        cv2.imshow("Camera feed", frame1)

    print(f"File saved as {filename} ")
    system(f"mv {filename} {path}")
    file_path = f"/home/kunal-kumar-sahoo/Programming/PySecurityCam/.Video-Files/{filename}"
    print(file_path)
    cam.release()
    output.release()
    cv2.destroyAllWindows()
    # database_access.append_data()
    file = open("credentials.txt", 'r')
    credentials = file.readlines()
    username = credentials[1]
    password = credentials[2]
    database_access.add_index(username, password, 'PySecurityCam', 'Logs', filename, file_path)
    file.close()
