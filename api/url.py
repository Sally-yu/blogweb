from django.urls import path
from . import views


app_name='api'
urlpatterns=[
    path('allnews/',views.allNews,name='allnews'),
    path('posttest/',views.postTest,name='posttest'),
]