import tkinter as tk
from tkinter import filedialog, messagebox
import pywhatkit as pk
import pyautogui
import time
import threading
import os

# Function to load phone numbers from a file
def load_numbers(file_path):
    try:
        with open(file_path, "r") as file:
            numbers = [line.strip() for line in file if line.strip()]
        return numbers
    except FileNotFoundError:
        messagebox.showerror("Error", "❌ File not found.")
        return []

# Function to send WhatsApp messages or images
def send_messages():
    numbers_file = entry_numbers.get()
    message = txt_message.get("1.0", tk.END).strip()
    image_path = entry_image.get()

    if not numbers_file:
        messagebox.showerror("Error", "❌ Please select a numbers file!")
        return

    # Load phone numbers
    phone_numbers = load_numbers(numbers_file)

    if not phone_numbers:
        messagebox.showwarning("Warning", "⚠️ No phone numbers found!")
        return

    if not message and not image_path:
        messagebox.showerror("Error", "❌ Please enter a message or select an image!")
        return

    # Get the current time
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    print(f"⏰ Scheduling message for {hour}:{minute}")

    messagebox.showinfo("Info", f"📤 Sending messages to {len(phone_numbers)} contacts...")

    def send():
        for number in phone_numbers:
            try:
                print(f"⏳ Sending to {number}...")

                # Send text message if provided
                if message:
                    pk.sendwhatmsg_instantly(number, message)
                    pyautogui.press("enter")

                # Send image if provided
                if image_path and os.path.exists(image_path):
                    print(f"📸 Sending image: {image_path} to {number}")
                    pk.sendwhats_image(number, image_path, "Image Sent")
                    pyautogui.press("enter")
                else:
                    print("❌ Image path is invalid or not provided.")

                print(f"✅ Message sent to {number}!")

            except Exception as e:
                print(f"❌ Error sending to {number}: {e}")

        print("🎯 Broadcast completed!")
        messagebox.showinfo("Completed", "✅ Broadcast completed successfully!")

    # Use threading to prevent GUI from freezing
    threading.Thread(target=send).start()

# Function to select the .txt file with numbers
def select_numbers_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        entry_numbers.delete(0, tk.END)
        entry_numbers.insert(0, file_path)
        check_send_button()

# Function to select an image file
def select_image_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg")]) # images must be in jpg format
    if file_path:
        entry_image.delete(0, tk.END)
        entry_image.insert(0, file_path)
        check_send_button()

# Function to check if conditions are met for enabling the send button
def check_send_button():
    numbers_file = entry_numbers.get()
    message = txt_message.get("1.0", tk.END).strip()
    image_path = entry_image.get()

 # If numbers file is selected and either message or image is provided, enable the send button
    if numbers_file and (message or image_path):
        btn_send.config(state=tk.NORMAL, bg="green", fg="white")
        btn_send.after(100, jump_button)  # Start jumping effect
    else:
        btn_send.config(state=tk.DISABLED, bg="gray", fg="white")
     
# Function to make the button "turn green" when enabled
def jump_button():
   btn_send.config(fg="green")

# Function to handle message input changes and update the button
def on_message_input_change(*args):
    check_send_button()

# GUI Layout
root = tk.Tk()
root.title("WhatsApp Automation with Messages or Images")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

# Select Numbers File
tk.Label(root, text="Select Numbers File (.txt) :", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
tk.Label(root, text="*", fg="red", font=("Helvetica", 12)).pack(pady=5)

frame_numbers = tk.Frame(root)
frame_numbers.pack(padx=10, pady=5)

entry_numbers = tk.Entry(frame_numbers, width=50, font=("Helvetica", 11))
entry_numbers.pack(side=tk.LEFT, padx=5)

btn_browse_numbers = tk.Button(frame_numbers, text="Browse", command=select_numbers_file, font=("Helvetica", 11))
btn_browse_numbers.pack(side=tk.LEFT)


# Message Entry
tk.Label(root, text="Enter Message (Optional if no image):", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
txt_message = tk.Text(root, width=70, height=5, font=("Helvetica", 11))
txt_message.pack(padx=10, pady=5)
txt_message.bind("<KeyRelease>", on_message_input_change)


# Select Image
tk.Label(root, text="Select Image (Optional if no message):", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=5)
frame_image = tk.Frame(root)
frame_image.pack(padx=10, pady=5)

entry_image = tk.Entry(frame_image, width=50, font=("Helvetica", 11))
entry_image.pack(side=tk.LEFT, padx=5)

btn_browse_image = tk.Button(frame_image, text="Browse", command=select_image_file, font=("Helvetica", 11))
btn_browse_image.pack(side=tk.LEFT)

# Send Button
btn_send = tk.Button(root, text="Send Messages", command=send_messages, bg="gray", fg="black", font=("Helvetica", 12, "bold"))
btn_send.pack(pady=15)

# Run the GUI
root.mainloop()
