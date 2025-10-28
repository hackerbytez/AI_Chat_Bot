import tkinter as tk
from tkinter import scrolledtext
import requests
import threading
import json

# API details
url = "https://chatgpt-api8.p.rapidapi.com/"
headers = {
    "Content-Type": "application/json",
    "x-rapidapi-host": "chatgpt-api8.p.rapidapi.com",
    "x-rapidapi-key": "YOUR_API_KEY_HERE" # Replace with your RapidAPI key
}

# Function to send a request
def ask(question):
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": question}
    ]
    try:
        response = requests.post(url, headers=headers, data=json.dumps(messages))
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0 and "content" in data[0]:
                return data[0]["content"]
            elif isinstance(data, dict) and "response" in data:
                return data["response"]
            else:
                return json.dumps(data, indent=2)
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

# Threaded function to handle chat
def send_message():
    user_input = entry.get().strip()
    if not user_input:
        return

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"You: {user_input}\n", "user")
    chat_box.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

    def get_response():
        bot_reply = ask(user_input)
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, f"Bot: {bot_reply}\n\n", "bot")
        chat_box.config(state=tk.DISABLED)
        chat_box.yview(tk.END)

    threading.Thread(target=get_response).start()

# GUI setup
root = tk.Tk()
root.title("AI Chat Bot (RapidAPI)")
root.geometry("600x600")
root.config(bg="#1e1e1e")

title_label = tk.Label(root, text="AI Chat Bot 🤖", font=("Arial", 20, "bold"), fg="white", bg="#1e1e1e")
title_label.pack(pady=10)

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), bg="#2d2d2d", fg="white", padx=10, pady=10)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_box.tag_config("user", foreground="#4FC3F7")
chat_box.tag_config("bot", foreground="#81C784")
chat_box.config(state=tk.DISABLED)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10, fill=tk.X, padx=10)

entry = tk.Entry(frame, font=("Arial", 14), bg="#2d2d2d", fg="white", insertbackground="white")
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(frame, text="Send", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                        activebackground="#66BB6A", activeforeground="white", command=send_message)
send_button.pack(side=tk.RIGHT)

root.mainloop()
