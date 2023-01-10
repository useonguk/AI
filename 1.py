# import cv2
# img = cv2.imread('data/Dog.jpg')
# cv2.imshow('image', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

import cv2 #패키지 들고오기

# cap = cv2.VideoCapture(0) # 0 = 첫번째 웹캠 불러오기 (영상파일 주소넣어도 가능(mp4파일 같은거))
# print(cap.isOpened()) # 열리면 참 아니면 거짓
# while(cap.isOpened()):
#     ret, frame = cap.read() # ret = 프레임이 받아와지면 참 안받아와지면 거짓/ frame = 객체로 만듬
#     if ret : # 객체가 생성됬으면
#         cv2.imshow('frame', frame) # 제목
#         if cv2.waitKey(1) & 0xFF == ord('q'): # q키 누르면 break해서 나감 
#             break
#     else:
#         break

# cap.release()
# cv2.destroyAllWindows()

import csv
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

print(cap.isOpened())
while(cap.isOpened()) :
    ret, frame = cap.read()
    if ret == True :
        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
    else : 
        break
cap.release()
out.release()
cv2.destroyAllWindows()