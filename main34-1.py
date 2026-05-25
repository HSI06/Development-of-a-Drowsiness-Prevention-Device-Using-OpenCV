import cv2                            # OpenCV 라이브러리 불러오기
from gpiozero import Buzzer           # GPIO 부저 제어 클래스 불러오기
import time                           # 시간 관련 라이브러리 불러오기

buzzerPin = Buzzer(16)                # GPIO 16번 핀에 부저 객체 생성

def main():
    camera = cv2.VideoCapture(-1)     # 웹캠 자동 탐지 후 열기
    camera.set(3, 640)
    camera.set(4, 480)

    face_xml = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    eye_xml  = cv2.data.haarcascades + 'haarcascade_eye.xml'
    face_cascade = cv2.CascadeClassifier(face_xml)
    eye_cascade  = cv2.CascadeClassifier(eye_xml)

    while camera.isOpened():
        _, image = camera.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray,
                                              scaleFactor=1.1,
                                              minNeighbors=5,
                                              minSize=(100, 100),
                                              flags=cv2.CASCADE_SCALE_IMAGE)
        print("faces detected Number: " + str(len(faces)))

        if len(faces):
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)  # 얼굴: 파란 사각형

                face_gray  = gray[y:y+h, x:x+w]
                face_color = image[y:y+h, x:x+w]

                eyes = eye_cascade.detectMultiScale(face_gray,
                                                    scaleFactor=1.1,
                                                    minNeighbors=5)

                if len(eyes) <= 1:  buzzerPin.on()   # 눈 1개 이하 → 부저 켜기
                else:               buzzerPin.off()  # 눈 2개 이상 → 부저 끄기

                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(face_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)  # 눈: 초록 사각형

        cv2.imshow('result', image)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
    buzzerPin.off()                   # 부저 강제 끄기

if __name__ == '__main__':
    main()
