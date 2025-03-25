import pywhatkit as pk
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

    message = "This is a test message sent to you through Python Whatsapp Automation"
    
    # Disaster Program Cover Image
    image_path_ci = "images/disaster_program.jpg"
    caption_ci = "Disaster Program"
    
    # Supply List for Each Community Member
    image_path_sl = "images/supply_list.jpg"
    caption_sl = "Supply List"

    for number in phone_numbers:
        try:
            # Send the message
            print(f"⏳ Sending to {number}...")
            pk.sendwhatmsg_instantly(number, message)
            pk.sendwhats_image(number, image_path_ci, caption_ci)
            
            # Wait for WhatsApp to load and press Enter
            pyautogui.press("enter")
            
            print(f"✅ Message sent to {number}!")

        except Exception as e:
            print(f"❌ Error sending to {number}: {e}")

print("🎯 Broadcast completed!")
