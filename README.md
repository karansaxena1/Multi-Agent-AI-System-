# 🤖💡 Multi-Agent AI System

Welcome to the **Multi-Agent AI System** – your intelligent assistant for automating complex medical and research workflows using multiple specialized AI agents, built **from scratch in pure Python**! 🐍💪

---

## 🔧 About the Project

This project was developed **without using any external AI frameworks** (like LangChain, Crewai, or AutoGen). Instead, it leverages **custom-built agents** managed via a powerful Python-based orchestration system 🧠⚙️.

Everything is stitched together with ❤️ and code – modular, maintainable, and fully transparent! 🙌

---

# Working Link 

https://multiagentaisystem.streamlit.app/

---

## 🚀 Features

Here's what your AI team can do:

### 📄✂️ Summarize Medical Text

![Screenshot 2025-04-17 104452](https://github.com/user-attachments/assets/639b722b-9145-4a8c-aa0f-b5953d38a31c)

- Quickly turn long medical documentation into short, concise summaries.
- Uses a main summarizer agent + a validator agent to ensure factual consistency ✅

### ✍️📝 Write and Refine Research Articles

![Screenshot 2025-04-17 104625](https://github.com/user-attachments/assets/0a89b108-fd65-41ba-90ef-babeb687fd06)

- Generate a full research article from a topic (and optionally, an outline).
- Automatically refine and validate the output before presenting it to the user ✨

### 🧹💉 Sanitize Medical Data (PHI)

![Screenshot 2025-04-17 104821](https://github.com/user-attachments/assets/53b7a9de-152e-44e7-af26-bb4dbf398bd2)

- Detect and remove personally identifiable information (PII/PHI) from medical data.
- Outputs a clean version plus validation to ensure compliance 🛡️🧽

---

Architecture
```bash
+-------------------+
|       User        |
+---------+---------+
          |
          | Interacts via
          v
+---------+---------+
|    Streamlit App  |
+---------+---------+
          |
          | Sends task requests to
          v
+---------+---------+
|  Agent Manager    |
+---------+---------+
          |
          +---------------------------------------------+
          |                      |                      |
          v                      v                      v
+---------+---------+  +---------+---------+  +---------+---------+
|  Summarize Agent  |  |  Write Article    |  |  Sanitize Data    |
|  (Generates summary)| |  (Generates draft)| |  (Removes PHI)    |
+---------+---------+  +---------+---------+  +---------+---------+
          |                      |                      |
          v                      v                      v
+---------+---------+  +---------+---------+  +---------+---------+
|Summarize Validator|  | Refiner Agent      |  |Sanitize Validator |
|      Agent        |  |  (Enhances draft)  |  |      Agent        |
+---------+---------+  +---------+----------+ +----------+--------+
          |                      |                      |
          |                      |                      |
          +-----------+----------+-----------+----------+
                      |                      |
                      v                      v
                +-----+-------+        +-----+-------+
                |   Logger    |        |   Logger    |
                +-------------+        +-------------+
```


## 🧠 How It Works

- 🧑‍💻 **Custom Agent System**: Agents are implemented using plain Python classes and methods – no third-party orchestration tools.
- 🔁 **AgentManager**: Handles retries, logs, and smooth execution of agent pipelines.
- 🕵️ **Validator Agents**: Each core task includes a validation agent for double-checking outputs.

---

## 🖥️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Core development |
| 🌱 Dotenv | Environment config |
| 🧰 Streamlit | UI interface |
| 🪵 Custom Logger | Error tracking |
| 📦 No AI Frameworks | Pure logic implementation |

---

## 📦 Installation

1. 🍴 Clone this repo:
```bash
git clone https://github.com/your-username/multi-agent-ai-system.git
cd multi-agent-ai-system
```
2. 📦 Install dependencies:
```bash
pip install -r requirements.txt
```
3. ⚙️ Add your .env file:
```bash
# .env
OPENAI_API_KEY=your_api_key_here
```
4. ▶️ Run the app:
```bash
streamlit run app.py
```
📁 Project Structure
```bash
multi-agent-ai-system/
│
├── agents/                # 🧠 All custom agents
├── utils/logger.py        # 🪵 Logging utility
├── app.py                 # 🚀 Main Streamlit app
├── .env                   # 🔐 Environment variables
└── README.md              # 📘 You're reading it!
```
# Made with ❤️ by Karan Saxena

## 🥳 Final Notes

This system was:

🧱 Built from the ground up

👨‍🔬 Tested for real medical scenarios

🌍 Designed to be extended for any domain

# "Build smart. Build simple. Build from scratch." 🔁🧠✨

