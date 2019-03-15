from django.urls import path
from . import views


app_name='api'
urlpatterns=[
    path('news<int:id>/',views.news,name='news'),
    path('news/',views.allNews,name='allNews'),
    path('posttest/',views.postTest,name='posttest'),
]