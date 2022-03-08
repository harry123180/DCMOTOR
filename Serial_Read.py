import serial
import time
import threading
import sys
COM_PORT = 'COM11'  # 請自行修改序列埠名稱
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES)
def job():
    while True:
        # 接收用戶的輸入值並轉成小寫
        choice = input('按1激磁、按2關、按e關閉程式  ').lower()
        msg = bytes(choice+'\n',encoding="ascii")
        ser.write(msg)



# 建立一個子執行緒
t = threading.Thread(target = job)

# 執行該子執行緒
t.start()

try:

    while True:
        start = time.time()
        while ser.in_waiting:
            mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
            print('控制板回應：', mcu_feedback)
            end = time.time()
            print(format(end - start))
except KeyboardInterrupt:
    ser.close()
    # 等待 t 這個子執行緒結束
    t.join()
    print('再見！')