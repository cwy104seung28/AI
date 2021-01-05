import cv2,time
from datetime import date,time,datetime,timedelta
import tkinter as tk

my_minute = int(input("請輸入分鐘："))
if my_minute > 60 :
    my_minute = int(input("請再輸入一次："))

currentTime = datetime.now()
userTime = timedelta(minutes = int(my_minute))
finalTime = currentTime + userTime
print (finalTime.strftime('%H:%M:%S'))

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    now = datetime.now()
    if finalTime.minute == now.minute and finalTime.second == now.second:
        window = tk.Tk()
        window.title('貼心提醒')
        window.geometry('500x300') 
        l = tk.Label(window, text='時間已到', font=('微軟正黑體', 12), width=30, height=2)
        l.pack()
        window.mainloop()
        break
    # print (now.strftime('%Y-%m-%d %H:%M:%S'))
    
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)  #正常視窗大小
    cv2.imshow('img', img)                     #秀出圖片
    if cv2.waitKey(30)== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
