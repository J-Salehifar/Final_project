from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class PostInline(admin.TabularInline):
    model = Post.auther.through
    extra = 0

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['get_image','title','get_authers','status','category','get_edit_date','get_create_date']
    list_filter = ['status','category','auther','create_date']
    search_fields = ['title','short_description','description']
    list_editable = ['title','status','category']
    inlines = [CommentInline]


    def get_image(self, obj):
        return mark_safe('<img src="{}" alt="{}"  width="100" height="100">'.format("/media/" + str(obj.img), str(obj.title)))   
    get_image.short_description = 'عکس پست'



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['get_post_title','get_user_name','status','get_create_date']
    list_filter = ['status','create_date']
    search_fields =['user__user__last_name','user__user__first_name','post__title']
    list_editable = ['status']
    readonly_fields = ['post','user','budy']
    


    def get_post_title(self,obj):
        try:
            return "%s" %(obj.post)
        except:
            return "---"

    get_post_title.short_description = 'عنوان پست'


    def get_user_name(self,obj):
        try:
            return "%s" %(obj.user)
        except:
            return "---"

    get_user_name.short_description = 'نویسنده دیدگاه'


