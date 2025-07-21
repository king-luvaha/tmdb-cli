# 🎬 TMDB CLI Movie App

A simple and stylish command-line interface (CLI) tool to fetch and display movies from [The Movie Database (TMDB)](https://www.themoviedb.org/) API.

Easily browse popular, top-rated, now playing, and upcoming movies directly in your terminal.

---

## 🚀 Features

- 🎞️ Fetches movies by category: `popular`, `top`, `playing`, `upcoming`
- 📊 Nicely formatted table output using `tabulate` and `colorama`
- 🔐 Secure API key management with `.env`
- ⚙️ Simple command-line interface

---

## 🧰 Requirements

- Python 3.7+
- TMDB API Key (Free)
- Internet connection

---
## 📁 Project Structure

```
tmdb-cli/
│
├── venv/                # Virtual environment
├── .env                 # Stores your TMDB API key
├── tmdb_app.py          # Main CLI script
├── requirements.txt     # List of dependencies
└── README.md            # README file
```

---

## 🛠️ Installation & Setup

### 1. Clone the Repository (or Create Folder)

```bash
git clone https://github.com/yourusername/tmdb-cli.git
cd tmdb-cli
````

Or manually create a folder and add the files.

---

### 2. Create & Activate Virtual Environment (Recommended)

```bash
python -m venv venv
```

- Activate it:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install requests python-dotenv colorama tabulate
```

---

### 4. Get a TMDB API Key

1. Sign up at [TMDB](https://www.themoviedb.org/signup)
2. Confirm your email and log in
3. Go to [https://www.themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)
4. Click **Create** under _API Key (v3 auth)_
5. Copy your API key

---

### 5. Create `.env` File

Create a file named `.env` in your project root and paste your API key:

```env
TMDB_API_KEY=your_tmdb_api_key_here
```

---

## ▶️ Usage

Run the CLI tool using:

```bash
python tmdb_app.py --type popular
```

### Available Types:

- `popular` – Most popular movies
- `top` – Top rated movies
- `playing` – Movies now playing in theaters
- `upcoming` – Movies coming soon

### Example:

```bash
python tmdb_app.py --type top
```

---

## 📷 Sample Output

```
🎬 TOP MOVIES
============================================================

╒════╤════════════════════════════════╤══════════════╤════════════╕
│ #  │ Title                          │ Release Date │ Rating     │
╞════╪════════════════════════════════╪══════════════╪════════════╡
│ 1  │ The Shawshank Redemption       │ 1994-09-23   │ 8.7 ⭐      │
│ 2  │ The Godfather                  │ 1972-03-14   │ 8.7 ⭐      │
│ …  │ …                              │ …            │ …          │
╘════╧════════════════════════════════╧══════════════╧════════════╛
```

---

## 💡 Optional: Make It Globally Executable (Windows)

1. Create a `tmdb-app.bat` file:

```bat
@echo off
python tmdb_app.py %*
```

2. Add the folder to your system `PATH`
3. Run from anywhere:

```bash
tmdb-app --type upcoming
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---


## Roadmap Project URL

URL: https://roadmap.sh/projects/tmdb-cli
