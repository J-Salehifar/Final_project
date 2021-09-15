from django.urls import path
from .views import post_view,detail_view

app_name='blog'

urlpatterns = [
    path('post_view/',post_view,name='post_view'),
    path('detail_view/<str:slug>/', detail_view, name='detail_view'),
    
]
