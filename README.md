# Django Snippet Saver
A Django application for saving code snippets in various programming languages.

## Prerequisites
- Python 3.x
- pip
- virtualenv

## Getting Started
To view the site as deployed on Heroku, you can visit <https://django-snippet-saver.herokuapp.com/>.

If you would like to run the site locally, please ensure that you have installed the prerequisites, then follow the steps below:
 
1. Clone this repository to your machine with `git clone http://github.com/mchlltt/django-snippet-saver.git`.
2. Navigate to the cloned directory.
3. Create a virtual environment with `virtualenv env`.
4. Activate the environment with `source env/bin/activate`.
5. Install the application requirements with `pip install -r requirements.txt`.
6. Make migrations with `python manage.py makemigrations`.
7. Run migrations with `python manage.py migrate`.
8. Start the server with `python manage.py runserver`.
5. The application will be running at `localhost:8000/`.

## Technologies Used
- Django (Web framework)
- SQLite (Local database)
- Bootstrap (Front-end framework)
- Heroku (Cloud platform)
- Heroku PostgreSQL (Cloud database)

## Author
Mich Elliott - [mchlltt](http://github.com/mchlltt)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.