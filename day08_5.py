import cv2
import  mediapipe as mp

# 이미지
def image(i_p):
    i = cv2.imread(i_p)
    cv2.putText(i,"cmh",(0, 50),cv2.FONT_ITALIC,2,(0, 50, 0),1)
    cv2.imshow('image', i)
    cv2.waitKey(0)
# 동영상
def video(i_p):
    v = cv2.imread(i_p)
    v2 = cv2.resize(v, (1280, 720))
    cv2.imshow('video', v2)
    cv2.waitKey(25)

# 웹캠 얼굴찾기
def webfind():
    cap = cv2.VideoCapture(0)
    mp_fd = mp.solutions.face_detection
    mp_draw = mp.solutions.drawing_utils
    fd = mp_fd.FaceDetection()
    while True:
        success, img = cap.read()
        if success:
            from_bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face = fd.process(from_bgr_to_rgb)
            if face.detections:
                for id, detection in enumerate(face.detections):
                    mp_draw.draw_detection(img, detection)
            cv2.imshow('title', img)
        cv2.waitKey(1)

# image('ia.jpg')
video('vd.mp4')
