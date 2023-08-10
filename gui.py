import tkinter as tk
import requests
from PIL import ImageTk, Image  

def send_message():
    webhook_url = webhook_entry.get()
    message_content = message_entry.get("1.0", "end-1c")

    payload = {
        "content": message_content
    }

    response = requests.post(webhook_url, json=payload)

    if response.status_code == 204:
        status_label.config(text="Message sent successfully!", fg="green")
        message_entry.delete("1.0", "end")
    else:
        status_label.config(text=f"Failed to send message. Status code: {response.status_code}", fg="red")

root = tk.Tk()
root.title("DWS Desktop")

webhook_label = tk.Label(root, text="Webhook URL:")
webhook_label.pack()

webhook_entry = tk.Entry(root)
webhook_entry.pack()

message_label = tk.Label(root, text="Message:")
message_label.pack()

message_entry = tk.Text(root, height=5, width=40)
message_entry.pack()

send_button = tk.Button(root, text="Send Message", command=send_message)
send_button.pack()

status_label = tk.Label(root, text="", fg="black")
status_label.pack()

root.mainloop()
