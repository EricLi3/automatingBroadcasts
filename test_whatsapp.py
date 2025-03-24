import pywhatkit
import pyautogui
import time

def load_numbers(file_path):
    try:
        with open(file_path, "r") as file:
            numbers = [line.strip() for line in file if line.strip()]
        return numbers
    except FileNotFoundError:
        print("❌ Error: File not found.")
        return []

# File path for the text file with phone numbers
file_path = "phone_numbers.txt"
phone_numbers = load_numbers(file_path)

# Get the current time
current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min
print(f"⏰ Scheduling message for {hour}:{minute}")

if not phone_numbers:
    print("⚠️ No phone numbers found!")
    
else:
    print(f"Sending messages to {len(phone_numbers)} contacts...")

    message = "Hello! This is a test message sent via WhatsApp automation."

    for number in phone_numbers:
        try:
            # Send the message
            print(f"⏳ Sending to {number}...")
            pywhatkit.sendwhatmsg_instantly(number, message)
            
            # Wait for WhatsApp to load and press Enter
            time.sleep(3)
            pyautogui.press("enter")
            
            print(f"✅ Message sent to {number}!")

        except Exception as e:
            print(f"❌ Error sending to {number}: {e}")

print("🎯 Broadcast completed!")
