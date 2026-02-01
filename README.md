# Django Financial Tracker

A comprehensive web-based financial tracking application built with Django that helps users manage their income, expenses, and financial goals.

🌐 **Live Application**  
👉 https://avishi03.pythonanywhere.com

---

## 🚀 Features

### 💰 Transaction Management
- Add income and expense transactions
- Edit and delete existing transactions
- Filter by category, type, and date range
- Paginated transaction list

### 📊 Dashboard
- Total income, expenses, and balance
- Monthly financial summary
- Recent transactions overview
- Category-wise expense breakdown
- Goal progress visualization

### 🎯 Goal Management
- Create financial goals with deadlines
- Track progress using visual indicators
- Automatic goal status (Active / Completed / Overdue)
- Edit and delete goals

### 📈 Reports & Analytics
- Filterable financial reports
- Category-wise income and expense analysis
- Monthly financial breakdown
- Custom date-range filtering

### 🎨 User Interface
- Responsive design using Tailwind CSS
- Clean and intuitive layout
- Flash messages for user actions
- Mobile-friendly UI

---

## 🛠 Technology Stack

- **Backend**: Django 5.x
- **Frontend**: HTML, Tailwind CSS (CDN)
- **Icons**: Font Awesome
- **Database**: SQLite (default)
- **Deployment**: PythonAnywhere (Cloud)

---

## 🌐 Cloud Deployment (PythonAnywhere)

This application is deployed and publicly accessible.

🔗 **Live URL**
https://avishi03.pythonanywhere.com


### Deployment Steps Followed

1. **Project Upload**
   - Project directory:
     ```
     /home/Avishi03/djfintracker
     ```

2. **Virtual Environment Setup**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
3. **WSGI Configuration**

import os
import sys

project_home = '/home/Avishi03/djfintracker'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'djfintracker.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

4. **Production Settings (settings.py)**

DEBUG = False

ALLOWED_HOSTS = [
    "avishi03.pythonanywhere.com",
]


5. **Database Migration**

python manage.py migrate


6. **Reload Web App**

Reloaded from PythonAnywhere Web dashboard


## 💻 Local Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Clone Repository
```bash
git clone 
cd Django-Financial-Tracker/djfintracker
```

### Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Apply Migrations
```bash
python manage.py migrate
```

### Run Development Server
```bash
python manage.py runserver
```

The application will be available at:
```
http://127.0.0.1:8000/
```

## 🔑 Key URLs
- `/` or `/finance/` – Dashboard
- `/finance/register/` – User Registration
- `/accounts/login/` – Login
- `/finance/transaction/` – Transactions
- `/finance/goal/` – Goals
- `/finance/report/` – Reports
- `/admin/` – Django Admin

## 🔒 Security Notes
Before deploying to production:
- Change `SECRET_KEY`
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Enable HTTPS
- Configure static files properly

## 📄 License
MIT License

## 👩‍💻 Author
Avishi
