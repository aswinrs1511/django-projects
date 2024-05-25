from django.db import models

# Create your models here.


'''
    to create table:
    > python manage.py makemigrations

    > python manage.py migrate
'''

#in Django we use class to define tables
class StudentDepartment(models.Model):
    DEPT_NAME = models.CharField(max_length=500)
    DEPT_DESC = models.CharField(max_length=500)


class StudentDetails(models.Model):
    STU_NAME=models.CharField(max_length=500)
    STU_EMAIL=models.CharField(max_length=500)
    STU_DEPT=models.CharField(max_length=500)
