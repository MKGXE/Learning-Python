import cv2
import mediapipe as mp

cap = cv2.VideoCapture('person.mp4')
mp_fd = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
fd = mp_fd.FaceDetection()          # 정확도 조정
 # 무한반복 (동영상 == 빠르게 여러 이미지를 출력)
while True:
    success, img = cap.read()
    # 동영상을 성공적으로 읽었으면 보여주기 전에 얼굴을 찾는다
    if success:
        from_bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)      # 얼굴찾기 정확도 향상을 위해 BGR -> RGB
        face = fd.process(from_bgr_to_rgb)      # 얼굴 찾기
    
        if face.detections:
            # 얼굴을 찾았다! ==> 사람 얼굴을 찾은 다음 하고 싶은 동작
            # 함수 사용하기
            for id, detection in enumerate(face.detections):
                # mp_draw.draw_detection(img, detection)      # 찾은 얼굴을 사각형 표시
                fd_box = detection.location_data.relative_bounding_box
                box = fd_box.xmin * img.shape[1], fd_box.ymin * img.shape[0], fd_box.width * img.shape[1], fd_box.height * img.shape[0]
                cv2.rectangle(img, box, (0,0,255), 2)
                cv2.putText(img, f'{detection.score[0]*100}', (box[0],box[1]), cv2.FONT_ITALIC, 2, (0,0,0), 2)

        cv2.imshow('title', img)
    if cv2.waitKey(20) & 0xFF == 27:
        # 동영상 waitKey 20~25
        # ESC키를 눌러 종료
        break    # 동영상 읽어줘