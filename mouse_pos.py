import pyautogui
import keyboard

# 특정 키 누를 때 마우스 위치 출력
while True:
    if keyboard.is_pressed('a'):
        x, y = pyautogui.position()
        print(f"Current mouse position: ({x}, {y})")
