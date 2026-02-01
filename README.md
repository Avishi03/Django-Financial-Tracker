# Django Financial Tracker

A comprehensive web-based financial tracking application built with Django that helps users manage their income, expenses, and financial goals.

## Features

### 💰 Transaction Management
- **Add Transactions**: Record income and expenses with categories
- **View Transactions**: Browse all transactions with advanced filtering
- **Edit & Delete**: Update or remove transactions as needed
- **Filtering Options**: Filter by type (Income/Expense), category, and date range
- **Pagination**: Easy navigation through large transaction lists

### 📊 Dashboard
- **Financial Overview**: Real-time calculation of total income, expenses, and balance
- **Monthly Statistics**: Track current month's income and expenses
- **Recent Transactions**: Quick view of your latest 5 transactions
- **Category Breakdown**: Visual representation of top expense categories
- **Goal Progress**: Monitor your financial goals with progress indicators

### 🎯 Goal Management
- **Create Goals**: Set financial targets with deadlines
- **Track Progress**: Visual progress bars showing goal completion
- **Goal Status**: Indicators for Active, Completed, and Overdue goals
- **Edit & Delete**: Manage your goals easily

### 📈 Reports & Analytics
- **Generate Reports**: Comprehensive financial reports with filtering
- **Category Analysis**: Breakdown of income and expenses by category
- **Monthly Breakdown**: View financial data by month
- **Custom Filters**: Filter reports by date range, type, and category

### 🎨 User Interface
- **Modern Design**: Beautiful, responsive UI built with Tailwind CSS
- **User-Friendly**: Intuitive navigation and clean interface
- **Message Framework**: Success and error notifications
- **Responsive**: Works seamlessly on desktop and mobile devices

## Technology Stack

- **Backend**: Django 5.2.5
- **Frontend**: HTML, CSS (Tailwind CSS via CDN)
- **Icons**: Font Awesome 6.4.0
- **Database**: SQLite (default, can be configured for PostgreSQL/MySQL)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Django-Financial-Tracker
```

### Step 2: Navigate to Project Directory

```bash
cd djfintracker
```

### Step 3: Create Virtual Environment (Recommended)

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

### Step 4: Install Dependencies

```bash
pip install -r ../requirements.txt
```

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

This allows you to access the Django admin panel.

### Step 7: Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### Getting Started

1. **Register an Account**: Navigate to `/finance/register/` to create a new account
2. **Login**: Use `/accounts/login/` to sign in to your account
3. **Dashboard**: View your financial overview on the main dashboard
4. **Add Transactions**: Click "Add Transaction" to record income or expenses
5. **Set Goals**: Create financial goals to track your savings targets
6. **Generate Reports**: Use the Reports section for detailed financial analysis

### Key URLs

- `/` or `/finance/` - Dashboard
- `/finance/register/` - User Registration
- `/accounts/login/` - User Login
- `/finance/transaction/` - Transaction List
- `/finance/transaction/add/` - Add Transaction
- `/finance/goal/` - Goal List
- `/finance/goal/add/` - Add Goal
- `/finance/report/` - Generate Reports
- `/admin/` - Django Admin Panel

## Project Structure

```
djfintracker/
├── djfintracker/          # Main project directory
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── finance/               # Finance app
│   ├── models.py          # Transaction and Goal models
│   ├── views.py           # View logic
│   ├── forms.py           # Form definitions
│   ├── urls.py            # App URL configuration
│   ├── admin.py           # Admin configuration
│   └── templates/         # HTML templates
│       ├── finance/       # Finance app templates
│       └── registration/  # Authentication templates
├── manage.py              # Django management script
└── db.sqlite3             # SQLite database (created after migration)
```

## Features in Detail

### Transaction Management

- **Transaction Types**: Income and Expense
- **Categories**: Custom categories for better organization
- **Date Tracking**: Record transactions with specific dates
- **Amount Tracking**: Precise decimal tracking for financial amounts

### Dashboard Analytics

- Total income and expense calculations
- Current balance (Income - Expense)
- Monthly statistics
- Category-wise expense breakdown
- Recent transaction history

### Goal Tracking

- Set target amounts and deadlines
- Visual progress indicators
- Automatic status updates (Active/Completed/Overdue)
- Progress percentage calculations

### Reporting

- Filterable financial reports
- Category-wise income and expense analysis
- Monthly financial breakdown
- Complete transaction listings

## Configuration

### Database

By default, the project uses SQLite. To use PostgreSQL or MySQL:

1. Update `DATABASES` in `settings.py`
2. Install the appropriate database adapter:
   - PostgreSQL: `pip install psycopg2`
   - MySQL: `pip install mysqlclient`

### Static Files

Static files are configured in `settings.py`. For production, consider using:
- `django.contrib.staticfiles` (already included)
- WhiteNoise for static file serving
- CDN for static assets

### Security Settings

**Important**: Before deploying to production:

1. Change `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Update `ALLOWED_HOSTS` with your domain
4. Configure proper database settings
5. Set up static file serving
6. Enable HTTPS

## Development

### Running Tests

```bash
python manage.py test
```

### Creating Migrations

```bash
python manage.py makemigrations
```

### Applying Migrations

```bash
python manage.py migrate
```

### Accessing Admin Panel

1. Create a superuser: `python manage.py createsuperuser`
2. Navigate to `/admin/`
3. Login with superuser credentials

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Developed as a comprehensive financial tracking solution.

## Acknowledgments

- Django Framework
- Tailwind CSS
- Font Awesome
- All contributors and users

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository.

---

**Happy Financial Tracking! 💰📊**
