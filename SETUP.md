# Quick Setup Guide

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Django-Financial-Tracker
   ```

2. **Navigate to project directory**
   ```bash
   cd djfintracker
   ```

3. **Create and activate virtual environment**

   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **Linux/Mac:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r ../requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## First Steps

1. Register a new account at `/finance/register/`
2. Login at `/accounts/login/`
3. Start adding your transactions and goals!

## Troubleshooting

### Port already in use
If port 8000 is already in use, run the server on a different port:
```bash
python manage.py runserver 8080
```

### Migration errors
If you encounter migration errors, try:
```bash
python manage.py migrate --run-syncdb
```

### Import errors
Make sure you're in the `djfintracker` directory and your virtual environment is activated.
