import serial
import time

ser = serial.Serial('COM3', 9600) # 'COM3' を適切なシリアルポートに置き換えてください
target_db = 40.0 # 目標dB値

def read_from_serial():
    while True:
        try:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                print(f"受信したデータ: {line}") # デバッグ用
                current_db = float(line)
                print("現在のdB値:", current_db)
                if abs(current_db - target_db) <= 5: # 目標dB値に±5dB以内の場合にクリア
                    print("クリア！")
                    break
        except ValueError as e:
            print(f"データの変換に失敗しました: {e}")
        except KeyboardInterrupt:
            print("終了")
            break

if __name__ == "__main__":
    time.sleep(2) # シリアル接続の安定化のために待機
    read_from_serial()
