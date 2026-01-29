# Python AI To-Do App

A simple to-do app built with Python (Flask backend) and HTML/JavaScript (frontend) that uses Claude AI to generate tasks.

## What You'll Learn

- **Python Backend**: Flask web framework, REST APIs
- **Frontend**: HTML, CSS, JavaScript, fetch API
- **AI Integration**: Calling Claude API from Python
- **Full-Stack**: How frontend and backend communicate

## Project Structure

```
├── app.py              # Python backend server (Flask)
├── index.html          # Frontend (HTML/CSS/JavaScript)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## How It Works

```
Browser (Frontend)          Python Server (Backend)          Claude AI
     │                              │                             │
     │── Add Task ───────────────>  │                             │
     │                              │── Save to memory            │
     │<─── Task Added ──────────────│                             │
     │                              │                             │
     │── Ask AI ──────────────────> │                             │
     │                              │── API Call ──────────────>  │
     │                              │                             │
     │                              │<── AI Response ─────────────│
     │<─── Tasks Generated ─────────│                             │
```

## Setup Instructions

### Step 1: Install Python
Make sure you have Python 3.8+ installed:
```bash
python --version
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- `flask` - Web framework for Python
- `flask-cors` - Allows frontend to talk to backend
- `anthropic` - Claude AI library

### Step 3: Set Up API Key (For Real Deployment)

For learning in Claude.ai, the API key is handled automatically.

For real deployment, you'd need to:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Or create a `.env` file:
```
ANTHROPIC_API_KEY=your-api-key-here
```

### Step 4: Run the Server
```bash
python app.py
```

You should see:
```
🚀 Server starting on http://localhost:5000
📝 Open your browser and go to http://localhost:5000
```

### Step 5: Open in Browser
Go to: `http://localhost:5000`

## Understanding the Code

### Python Backend (app.py)

**What is Flask?**
Flask is a Python library that lets you create web servers.

**Key Concepts:**

1. **Routes** - URLs that do things
   ```python
   @app.route('/api/tasks', methods=['GET'])
   def get_tasks():
       return jsonify(tasks)
   ```
   - When browser visits `/api/tasks`, this function runs
   - Returns all tasks as JSON

2. **HTTP Methods**
   - `GET` - Read data
   - `POST` - Create new data
   - `PUT` - Update data
   - `DELETE` - Delete data

3. **API Endpoints**
   - `/api/tasks` (GET) - Get all tasks
   - `/api/tasks` (POST) - Add new task
   - `/api/tasks/<id>` (PUT) - Toggle task
   - `/api/tasks/<id>` (DELETE) - Delete task
   - `/api/ask-ai` (POST) - Ask Claude AI

### Frontend (index.html)

**How Frontend Talks to Backend:**

```javascript
// JavaScript makes HTTP request to Python
const response = await fetch('http://localhost:5000/api/tasks');
const tasks = await response.json();
```

This is called a **REST API** call.

## Common Commands

**Run the server:**
```bash
python app.py
```

**Stop the server:**
Press `Ctrl + C`

**Install new Python package:**
```bash
pip install package-name
```

**Check installed packages:**
```bash
pip list
```

## Next Steps for Learning

### Beginner Level (You are here!)
- ✅ Understand how Flask works
- ✅ Learn REST APIs (GET, POST, PUT, DELETE)
- ✅ See how frontend and backend connect

### Intermediate Level
- Add a **database** (SQLite or PostgreSQL) instead of storing tasks in memory
- Add **user authentication** (login/signup)
- Deploy to **Heroku** or **Railway**

### Advanced Level
- Learn **FastAPI** (modern Python framework)
- Add **websockets** for real-time updates
- Build more complex AI features

## Troubleshooting

**Error: "Port 5000 is already in use"**
- Another app is using port 5000
- Kill it or change port in `app.py`: `app.run(debug=True, port=5001)`

**Error: "No module named flask"**
- Run: `pip install -r requirements.txt`

**Error: "CORS policy"**
- Make sure `flask-cors` is installed
- Check that `CORS(app)` is in `app.py`

**Tasks disappear when server restarts**
- This is normal! Tasks are stored in memory
- To persist, you need a database (next step in learning)

## Deployment Options

When ready to deploy (make it public):

1. **Railway.app** (Easiest)
   - Connect GitHub repo
   - Auto-deploys

2. **Render.com**
   - Free tier available
   - Good for beginners

3. **Heroku**
   - Classic choice
   - Free tier removed but still popular

4. **PythonAnywhere**
   - Python-specific hosting
   - Very beginner-friendly

## Resources for Learning

- Flask Official Docs: https://flask.palletsprojects.com/
- Anthropic API Docs: https://docs.anthropic.com/
- REST API Tutorial: https://restfulapi.net/

## Questions?

Common beginner questions:

**Q: Why do I need both Python AND JavaScript?**
A: Python runs the server (backend), JavaScript runs in the browser (frontend). They work together.

**Q: Can I do everything in Python?**
A: Not easily. Browsers only understand HTML/CSS/JavaScript for the visual part.

**Q: What's the difference between Flask and Django?**
A: Flask is simple and flexible. Django is bigger with more built-in features. Start with Flask.

**Q: How do I add a database?**
A: Check out SQLAlchemy or use SQLite. That's your next learning step!
