
# News Aggregator Project

This is a news aggregator application built with Django. The project fetches and aggregates news from various sources and displays them in a user-friendly interface.

## Features
- Fetches news articles from multiple sources.
- Displays articles with titles, descriptions, and links to the original sources.
- Categorizes news based on topics.
- User authentication for saving preferred news sources.

## Requirements
- Python 3.x
- Django 4.x or higher
- Requests library for fetching news (or any other API client you use)

## Installation

Follow these steps to set up the project on your local machine:

### 1. Clone the repository
Clone the project repository to your local machine using:

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create and activate a virtual environment

You can create a virtual environment using `venv` (if you don't have one set up already):

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Install required dependencies

Install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file is not yet available, you can manually install Django and any other libraries (like `requests` for fetching news) with:

```bash
pip install django requests
```

### 4. Set up the database

Run the following commands to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (optional)

If you want to access the admin panel, create a superuser with:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the admin credentials.

### 6. Run the development server

Start the Django development server with:

```bash
python manage.py runserver
```

Thank you
