# Power TODO backend

Welcome to Awesome Todo List App! This is a simple and intuitive to-do list application built with React Native and Django, utilizing Expo to support both web and mobile platforms.

## Live

[Frontend](https://github.com/lucasalberto01/power-todo-expo)

[API](https://power-todo.herokuapp.com/api)

## Features

- Add, edit, and delete tasks
- Mark tasks as completed
- Easy-to-use user interface

## Technologies Used

- Django (<https://github.com/django/django>)
- Django REST Framework (<https://github.com/encode/django-rest-framework>)
- Mysql (<https://github.com/PyMySQL/mysqlclient>)

## Installation

Before getting started, make sure you have the following prerequisites:

- Python (<https://www.python.org/downloads/>)

## Setup

1. Clone the repository

    ```bash
    git clone https://github.com/lucasalberto01/power-todo-api.git
    ```

2. Create a virtualenv

    ```bash
    python -m venv .venv
    ```

3. Activate the virtualenv

    ```bash
    source .venv/bin/activate
    ```

4. Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

5. Make migrations

    ```bash
    python todo/manage.py makemigrations
    ```

6. Run migrations

    ```bash
    python todo/manage.py migrate
    ```

7. Create super user

    ```bash
    python todo/manage.py createsuperuser
    ```

8. Run the server

    ```bash
    python todo/manage.py runserver
    ```

## Configuration

The application uses environment variables for configuration. Create a `.env` file in the frontend directory and add the following variables:

```text
DJANGO_SECRET_KEY=< key of password encrypt >
CLEARDB_DATABASE_URL='mysql://root:root@localhost:3306/todo'
```

> Obs: On localhost the system automatically creates a database in sqlite3 for you to use

## Contributing

Contributions are welcome! If you find any issues or want to contribute enhancements, please feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Django](https://www.djangoproject.com) community for the powerful web framework
- [Django REST Framework](https://www.django-rest-framework.org) for the flexible toolkit for building Web APIs
- [dj_rest_auth](https://dj-rest-auth.readthedocs.io/en/latest/) for the awesome authentication and registration tools
- [Mysql](https://www.mysql.com) for the world's most popular open source database

