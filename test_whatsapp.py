import pywhatkit
import pyautogui
import time

# Get the current time
current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min
print(f"⏰ Scheduling message for {hour}:{minute}")

try:
    pywhatkit.sendwhatmsg_instantly("+15089813950","message: hello fuck you")
    
    time.sleep(5)  # Wait for WhatsApp Web to open
    pyautogui.press("enter")  # Simulate pressing "Enter" to send the message
    
    print("✅ Message sent successfully!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    
    