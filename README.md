# Django Sample Meeting Planner App

guide source:

https://www.pluralsight.com/courses/django-getting-started

### Part 1
created website app

add website to INSTALLED_APPS

added some simple views in website

mapped views to meeting_planner urls

### Part 2
created meetings app

add meetings to INSTALLED_APPS

created Meeting class with title, date, start, duration in meeting.models

added admin.site.register(Meeting) in meetings.admin

added __self__ in Meeting class (for admin view)

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`

### Part 3

created Room class with name, floor, room number in meetings.model

add room object foreign key in Meetings class

added admin.site.register(Room) in meetings.admin

added __self__ in Meeting class (for admin view)

cleaned db and migrations

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`

### Part 4

added templates folder for the html files of the website app

added templates folder for the html files of the meetings app

updated views for the template html files

added urlpatterns

get_object_or_404 for meeting detail view

