## Running this project 

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal, run the following command in the base directory of this project

```
virtualenv env
```

Activate the vitural enviroment, then install the project dependencies with

```
pip install -r requirements.txt
```

Apply django migrations **Note:** The *"migrate"* is not required because de django_migrations already exists in the db.sqlite3 file.

```
python manage.py migrate
```

Then create a super user **Note:** The *"createsuperuser"* are not required because a usere already exist in the db.sqlite3 file.
*"username: admin / pass: DeV.2017"*

```
python manage.py createsuperuser
```

Now you can run the project with this command

```
python manage.py runserver 0:8686
```

---



## Running this project with Docker

Build service in your project directory with

```
docker-compose build
```

Create and start the container with

```
docker-compose up -d
```

Apply django migrations **Note:** The *"migrate"* is not required because de django_migrations already exists in the db.sqlite3 file.

```
docker-compose exec web python manage.py migrate
```

Then create a super user **Note:** The *"createsuperuser"* are not required because a usere already exist in the db.sqlite3 file.
*"username: admin / pass: DeV.2017"*

```
docker-compose exec web python manage.py createsuperuser
```

*"The projects is by default in the port localhost:8686"*

---