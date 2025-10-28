# 🤖 AI Chat Bot (Python + RapidAPI)

A modern **AI Chat Bot** built using **Python**, **Tkinter GUI**, and **RapidAPI ChatGPT API**.  
It allows real-time interaction with an AI assistant directly from a desktop app.


## 🧠 Features

- 🗨️ Chat with an AI assistant powered by ChatGPT API  
- 🪶 Beautiful Tkinter-based GUI with dark theme  
- ⚡ Asynchronous message handling using `threading`  
- 🧰 Lightweight and easy to run (only requires `requests` library)  
- 🔑 Uses **RapidAPI** for secure API access  

---

## 📸 Screenshot

![AI Chat Bot Preview](/assets/aichatbot.png)

*(Add your screenshot image here — name it `aichatbot.png` and place in `/assets` folder)*


## Tech Stack

| Component | Description |
|------------|--------------|
| **Language** | Python |
| **Libraries** | Tkinter, Requests |
| **API** | RapidAPI ChatGPT |
| **Concepts Used** | Threading, GUI Events, HTTP POST |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/hackerbytez/AI_Chat_Bot.git
cd AI_Chat_Bot
````

### 2️⃣ Install Dependencies

```bash
pip install requests
```

*(Tkinter is pre-installed in Python on most systems)*


### 3️⃣ Get Your RapidAPI Key

1. Go to [RapidAPI ChatGPT API](https://rapidapi.com/hub)
2. Create a free account or log in.
3. Subscribe to the **ChatGPT API** (e.g., `chatgpt-api8`).
4. Copy your **X-RapidAPI-Key**.


### 4️⃣ Add Your API Key

Open `ai_chat_bot.py` and replace this line:

```python
"x-rapidapi-key": "YOUR_API_KEY"
```

with your actual key:

```python
"x-rapidapi-key": "c52b9ee71fmsh708bc1e2ddd08c7p10037ajsndad36274191c"
```


### 5️⃣ Run the App

```bash
python ai_chat_bot.py
```

Then start chatting with your AI bot! 💬


##  Project Structure

```
AI_Chat_Bot/
│
├── ai_chat_bot.py         # Main GUI Chat Bot code
├── assets/
│   └── aichatbot.png     # (Optional) Screenshot
├── README.md            # Project documentation
 
```


## 🖥️ GUI Preview

* Dark themed chat window
* Scrollable text area
* Input field with "Send" button
* Real-time AI replies


## 🧑‍💻 Author

**Uday Raut**
💼 GitHub: [@hackerbytez](https://github.com/hackerbytez)
🌐 Project Repo: [AI Chat Bot](https://github.com/hackerbytez/AI_Chat_Bot)


## 🪪 License

This project is open-source under the [MIT License](LICENSE).

---

### ⭐ If you like this project, give it a star on GitHub! ⭐
