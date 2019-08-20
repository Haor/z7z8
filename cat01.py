
import cv2

#Haar模型位置
catPath = "/lib/python3.7/site-packages/cv2/data/haarcascade_frontalcatface_extended.xml"
face_cascade = cv2.CascadeClassifier(catPath)


# 调用摄像头摄像头
cap = cv2.VideoCapture(0)

while(True):
    # 获取摄像头的画面
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    img = frame
    for (x,y,w,h) in faces:
    	# 画出猫猫的脸框，蓝色，画笔宽度2
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #用红字标注
        cv2.putText(img,'Cat',(x,y-7), 3, 1.2, (0, 0, 255), 2, cv2.LINE_AA)
        
	# 实时展示效果画面
    cv2.imshow('frame2',img)
    # 每5毫秒监听一次键盘动作
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 关闭所有窗口
cap.release()
cv2.destroyAllWindows()
