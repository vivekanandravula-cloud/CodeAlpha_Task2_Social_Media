# CodeAlpha Internship — Task 2: Social Media Platform

SocialHub is a mini social media application built with HTML, CSS, JavaScript, Python, Django, and SQLite.

## Features
- User registration, login, and logout
- User profiles with editable bio, location, and website
- Create and delete your own posts
- Comment on posts
- Like and unlike posts
- Follow and unfollow users
- Community feed and individual profile pages
- SQLite database for users, profiles, posts, comments, likes, and follows

## Setup (macOS / Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Setup (Windows)
```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

Optional admin account: `python manage.py createsuperuser`, then visit `/admin/`.

## Technologies
Frontend: HTML, CSS, JavaScript  
Backend: Python, Django  
Database: SQLite

## Internship
Organization: CodeAlpha  
Task: Task 2 — Social Media Platform

This is an educational demo. Configure a secure secret key, `DEBUG=False`, and allowed hosts before production deployment.
