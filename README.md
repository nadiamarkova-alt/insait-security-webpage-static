# INSAIT Security Research Group Website

A Django-based website for the INSAIT Security Research Group, featuring research topics, team members, publications, and contact information.

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

## Installation

### 1. Navigate to the project directory

```bash
cd "Security Group Webpage"
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Navigate to the Django project directory

```bash
cd securitywebpage
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Populate the database with sample data

```bash
python manage.py seed_data
```

This adds:
- 5 research topics
- 8 team members
- 8 publications

### 8. Run the development server

```bash
python manage.py runserver
```

The site will be available at: http://127.0.0.1:8000

## Project Structure

```
Security Group Webpage/
├── requirements.txt
├── venv/
└── securitywebpage/
    ├── manage.py
    ├── db.sqlite3
    ├── insait_security_group_webpage/   # Project settings
    ├── core/                             # Main app
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   └── management/commands/seed_data.py
    ├── templates/
    │   ├── base.html
    │   └── core/
    │       ├── home.html
    │       ├── research.html
    │       ├── members.html
    │       ├── publications.html
    │       └── contact.html
    ├── static/
    │   ├── css/style.css
    │   └── js/main.js
    └── media/
```

## Useful Commands

| Command | Description |
|---|---|
| `python manage.py migrate` | Apply database migrations |
| `python manage.py makemigrations` | Create new migrations after model changes |
| `python manage.py seed_data` | Populate database with sample data |
| `python manage.py runserver` | Start development server |
| `python manage.py collectstatic` | Collect static files for production |

## Features

- **Home page** with stats and research highlights
- **Research** page with topic cards
- **Members** page with photo cards and contact links
- **Publications** page with year filtering and pagination
- **Contact** page with form and group information
- **Responsive design** with Bootstrap 5 and custom CSS
- **SEO optimized** with Open Graph and Twitter Card meta tags
