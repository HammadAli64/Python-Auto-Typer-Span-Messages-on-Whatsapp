import pyautogui
import time
# Messgae you want to send
message = "I am Sorry"
count = 3 # Number of messages to send

# Wait a few seconds before starting (switch to WhatsApp Web manually)
time.sleep(5)

for _ in range(count):
    pyautogui.typewrite(message)  # Type the message
    pyautogui.press("enter")  # Press Enter to send
    time.sleep(1)  # Small delay before sending the next message
