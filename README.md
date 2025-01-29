# Book Manager Backend

This is the backend of the **Book Manager** application, built with **Django** and designed to manage book-related data and book lists. It provides RESTful APIs for managing books, creating book lists, and adding/removing books from lists.

## Features

- **Books API**: Allows you to view the list of all available books.
- **Book Lists API**: Enables users to create and manage their own book lists, including adding or removing books from lists.
## Requirements

- Python 3.8+
- Django 4.0+
- Django REST Framework
- SQLite (default database)

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/raheemiqram/book-manager-backend.git
   cd book-manager-backend

2. **Create a virtual environment:**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install the dependencies**
    ```bash
   pip install -r requirements/base.txt # On windows > pip install .\requirements\base.txt
   
4. **Migrate the database**
    ```bash
   python manage.py migrate
   
5. **Add Testing data**
    ```bash
   python manage.py seed_books # on windows  python .\manage.py seed_books

6. **Run the development server**
    ```bash
   python manage.py runserver
