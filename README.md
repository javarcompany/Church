# Church Project

Welcome to the Church Project! This project aims to create a comprehensive web application for managing church-related activities, including member management, event scheduling, sermon uploads, and more. The project is built using Django, a high-level Python web framework.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Member management: Add, update, and delete church members.
- Event scheduling: Create and manage church events and activities.
- Sermon uploads: Upload and manage sermon files.
- Image uploads: Upload images and retrieve image sizes.
- Admin panel: Manage the application via Django's built-in admin interface.

## Requirements

- Python 3.x
- Django 3.x or later
- Pillow library for image handling

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/church-project.git
   cd church-project
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Admin Panel:** Navigate to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created.
- **Upload Images and Files:** Use the admin panel to upload images and files, which will automatically save the file sizes.

## Project Structure

```
church-project/
│
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   ├── upload.html
│   │   └── image_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── church_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
├── media/
├── templates/
├── manage.py
└── requirements.txt
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
