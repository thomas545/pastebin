
# raseedi
### Documentation:

1. [Django](https://docs.djangoproject.com/en/2.0/releases/2.0/)
2. [Django Rest Framework](https://www.django-rest-framework.org/)

### Installation:

##### -> you must install Elastic Search on your computer (you can use brew)

##### System Dependencies:

1. Install git on Linux:  
`sudo apt-get install -y git`
2. Clone or download this repo.
3. Install pip and vitualenv on Linux:  
`sudo apt-get install -y virtualenv`  
`sudo apt-get install -y python3-pip`
4. Create a virtual environment on Linux or Mac:  
`virtualenv -p python3 ~/.virtualenvs/raseedi`
5. Activate the virtual environment on Linux or Mac:  
`source ~/.virtualenvs/raseedi/bin/raseedi`
6. Install requirements in the virtualenv:  
`pip3 install -r requirements.txt`
7. Make Django database migrations:
`python manage.py makemigrations`  
then: `python manage.py migrate`

##### Use admin interface:
2. Run the project locally:  
`python manage.py runserver`
3. Navigate to: `http://localhost:8000/admin/`
 

### Admin Credentials
### Username: `admin`  
### Password: `123` 


