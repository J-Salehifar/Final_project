from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from .utils import (
                    GENDER_TYPE,
                    resume_file_path,
                    check_is_digit,
                    )

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='کاربر',on_delete=models.CASCADE,related_name='profile')
    create_date = jmodels.jDateTimeField(verbose_name="تاریخ عضویت", auto_now_add=True)
    age = models.PositiveSmallIntegerField(verbose_name='سن', null=True)
    national_code =  models.CharField(verbose_name='کد ملی', max_length=10, validators=[check_is_digit])
    mobile_number = models.CharField(verbose_name='تلفن همراه', max_length=11,validators=[check_is_digit])
    bio = models.TextField(verbose_name='درباره من', null=True,blank=True)
    gender = models.CharField(verbose_name='جنسیت',choices=GENDER_TYPE,max_length=1)
    is_auther = models.BooleanField(verbose_name='نویسنده است؟',default=False)
    resume = models.FileField(verbose_name='رزومه',upload_to=resume_file_path, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

    def get_username(self):
        return self.user.username
    get_username.short_description = 'نام کاربری'

    def get_first_name(self):
        return self.user.first_name
    get_first_name.short_description = 'نام'

    def get_last_name(self):
        return self.user.last_name
    get_last_name.short_description = 'نام خانوادگی'

    def get_email(self):
        return self.user.email
    get_email.short_description = 'ایمیل'

    def get_create_date(self):
        return self.create_date.strftime('%H:%m - %Y/%m/%d')
    get_create_date.short_description = 'تاریخ ایجاد'

    def get_full_name(self):
        try:
            return "%s %s" %(self.user.first_name, self.user.last_name)
        except:
            return "---"

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'