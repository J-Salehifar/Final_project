from django.contrib import admin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import F, Q

def resume_file_path(instance, filename):
    return 'resume-files/%s.%s' %(instance.user, filename.split(".")[-1])   


male = 'M'
female = 'F'
other = 'O'
GENDER_TYPE =[
    (male, 'آقا'),
    (female,'خانم'),
    (other,'سایر'),
]


def check_is_digit(value):
    if not value.isdigit():
        raise ValidationError("مقدار ورودی باید از عددی باشد")

