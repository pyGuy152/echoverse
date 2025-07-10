# 🌌 EchoVerse

**EchoVerse** is a collaborative Discord bot for world-building, branching narratives, and interactive storytelling. It allows communities to craft evolving fictional universes together — one prompt, one character, and one vote at a time.

---

## 🚀 Features

- 🏙️ **World Creation** – Create shared universes with unique settings, timelines, and rules.
- 🧙‍♀️ **Character Builder** – Develop original characters tied to specific worlds.
- 🗺️ **Lore Wiki** – Automatically extract and organize lore based on user-generated content.
- 📚 **Prompt Engine** – Generate interactive prompts to spark creativity.
- 🧠 **Branching Storylines** – Let your community vote on what happens next.
- 🔗 **FastAPI Backend** – For future integration with websites, lore viewers, and AI modules.

---

## 📦 Tech Stack

| Component   | Tech Used       |
|------------|-----------------|
| Bot        | `discord.py` |
| Backend    | `FastAPI` (Python) |
| Database   | `PostgreSQL` |
| Frontend (planned) | TBD |

---

## 📁 Project Structure

```
echoverse/
├── bot/
│   ├── main.py                  # Discord bot entrypoint
│   ├── commands/                # Slash commands
│   └── utils/                   # NLP tools, vote logic, etc.
├── api/
│   └── fastapi_app.py           # REST API for worlds/characters
├── .gitignore                   
├── requirements.txt
└── README.md
```

---

## 🧠 API (FastAPI)

Base URL: `https://echoverse.codewasabi.xyz/api/v1` 

> Full API documentation available at `/docs` and `/redoc`.

---

## 🛠️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/pyGuy152/echoverse.git
cd echoverse
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create `.env` file
```env

```

### 4. Run the Discord Bot
```bash
python3 bot/main.py
```

### 5. Run the FastAPI Backend
```bash
uvicorn api.fastapi:app --reload
```

---

## 🧪 Example Commands (Discord)

```bash

```

---

## 📌 Roadmap

- [ ] Create worlds and characters
- [ ] Generate prompts and store responses
- [ ] Vote-based branching system
- [ ] Lore wiki extraction via NLP
- [ ] Web lore explorer (React)
- [ ] AI-enhanced prompt system

---

## 👨‍💻 Developer Notes

- All data is saved in Postgres db. Schema will be avalible soon.
- Use the FastAPI routes to debug or export world data.

---

