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

created Meeting class with title varchar and date ate in meeting.models

`python manage.py makemigrations`

`python manage.py migrate`

added admin.site.register(Meeting) in meetings.admin

`python manage.py createsuperuser`

added Meetings in admin interface

### Part 3

