from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import RelatedField
from django_jalali.db import models as jmodels
from django.db.models.deletion import CASCADE
from accounts.models import Profile
from .utils import post_image_path, STATUS_TYPE, CATEGORY_TYPE
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    slug = models.SlugField(null=True, allow_unicode=True, unique=True)
    auther = models.ManyToManyField(to=Profile, verbose_name='نویسنده', blank=True, related_name="posts")
    create_date = jmodels.jDateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True)
    edit_date = jmodels.jDateTimeField(verbose_name='تاریخ ویرایش', auto_now=True)
    title = models.CharField(verbose_name='عنوان',max_length=50)
    img = models.ImageField(verbose_name='عکس',upload_to=post_image_path)
    short_description = models.CharField(verbose_name='توضیحات خلاصه',max_length=300)
    description = RichTextField(verbose_name='توضیحات')
    status = models.PositiveSmallIntegerField(verbose_name='وضعیت',choices=STATUS_TYPE,default=3)
    category = models.PositiveSmallIntegerField(verbose_name='دسته بندی', choices=CATEGORY_TYPE, default=3,null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    def get_create_date(self):
        return self.create_date.strftime('%H:%m - %Y/%m/%d')
    get_create_date.short_description = 'تاریخ ایجاد'


    def get_edit_date(self):
        return self.edit_date.strftime('%H:%m - %Y/%m/%d')
    get_edit_date.short_description = 'تاریخ ویرایش'


    def get_authers(self):
        authers = ''
        for auther in self.auther.all():
            authers = authers  + '  ' + str(auther)
        return authers
    get_authers.short_description = 'نویسندگان'


    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        ordering = ['-create_date']


class Comment(models.Model):
    post = models.ForeignKey(to=Post,verbose_name='پست', on_delete=CASCADE,related_name='comments')
    user = models.ForeignKey(to=Profile,verbose_name='کاربر', on_delete=models.SET_NULL, null=True,related_name='comments')
    create_date = jmodels.jDateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True)
    budy = models.TextField(verbose_name='متن دیدگاه')
    status = models.PositiveSmallIntegerField(verbose_name='وضعیت',choices=STATUS_TYPE,default=3)

    def __str__(self):
        return "عنوان : %s - نویسنده : %s" %(self.post, self.user)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title, allow_unicode=True)
    #     super().save(*args, **kwargs)
    
    
    def get_create_date(self):
        return self.create_date.strftime('%H:%m - %Y/%m/%d')
    get_create_date.short_description = 'تاریخ ایجاد'


    class Meta:
        verbose_name = 'دیدگاه'
        verbose_name_plural = 'دیدگاه ها' 
        ordering = ['-create_date']   

