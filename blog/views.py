from django.contrib import messages
from accounts.forms import ProfileForm
from django import forms
from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm, CommentForm


def post_view(request):
    template_name='blog/post_view.html'
    context = {}
    context['posts_count'] = Post.objects.all().count()
    context['published_posts'] = Post.objects.filter(status = 1)
    context['comments_count'] = Post.objects.filter(status = 1)

    initial_auther = {
        'auther' : request.user
        }
    if request.user.is_authenticated :
        if request.user.profile.is_auther == True :
            form = PostForm(request.POST or None,request.FILES or None,initial=initial_auther)
            context['form'] = form
            if request.method == 'POST':
                if form.is_valid():
                    form.save()
                    return redirect('blog:post_view')
                else:
                    form = PostForm()
            return render(request,template_name,context)
         
    return render(request,template_name,context)

    
def detail_view(request,slug):
    template_name='blog/detail_view.html'
    context = {}
    post_detail = Post.objects.get(slug=slug)
    comments = post_detail.comments.filter(status = 1)
    context['post_detail'] = post_detail
    context['comments'] = comments

    initial_user = {
        'post': post_detail,
        'user' : request.user
        }
    if request.user.is_authenticated :
        form = CommentForm(request.POST or None,request.FILES or None,initial=initial_user)
        context['form'] = form
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request,'نظر شما با موفقیت ثبت شد')
                return redirect('blog:post_view')
            else:
                form = PostForm()
        return render(request,template_name,context)

    return render(request,template_name,context)