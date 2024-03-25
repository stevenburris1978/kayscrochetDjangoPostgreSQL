## INF601VA - Advanced Programming in Python
# Steven Burris
# 11-10-2023
# *Final Project SBurris*
# *Kay's Crochet App*

# Github commits to Main Branch instead of Master at: 
[Gituhb](https://github.com/stevenburris1978/KaysCrochetAppDjangoSBurris/tree/main)
# This code can be deployed without change locally or through heroku at domain: 
[Kayscrochet](https://www.kayscrochet.us)
# *Description*
### With this app, admin can add an item that has title, description, images, price and set choices to vote on future items that will be created.
### Admin can also see likes, get new customer orders emailed to them, and see the details of an order in the admin customer_order table.
### Users can log in and see the items, like the items, vote on the choices, search items, and buy the items with an invoice that gets emailed to them.
# *Social App Install Instructions*
Please copy the following command in the terminal for all the package downloads needed to run the program:
```
pip install -r requirements.txt
```
# How to set up .env variables - they need to be in a .env root directory with your keys and passwords for local development to work
DJANGO_SECRET_KEY=
AWS_AKEY=
AWS_SECRET_ACCESS_KEY=
STRIPE_PUBLIC_KEY=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
DJANGO_EMAIL_HOST=
DJANGO_EMAIL_HOST_USER=
DJANGO_EMAIL_HOST_PASSWORD=
DJANGO_EMAIL_PORT=
DJANGO_EMAIL_USE_TLS=
AWS_STORAGE_BUCKET_NAME=
AWS_S3_REGION_NAME=
DATABASE_URL= is the postgresql url from heroku
# How to set up database
(this will create any SQL entries that need to go into the database)
```
python manage.py makemigrations kayscrochetapp
```
(this will show tables created)
```
python manage.py sqlmigrate kayscrochetapp 0001
```
(this will apply the migrations)
```
python manage.py migrate
```

# How to create the main admin user
(this will create the administrator login to log into Kay's Crochet App administration page)
```
python manage.py createsuperuser
```

# How to start app
```
python manage.py runserver
``` 
and go to [ App home page](http://127.0.0.1:8000)

# This is the link to go to the admin page to add, edit, and delete the Social App post items
Administration url : [Administration url](http://127.0.0.1:8000/admin)