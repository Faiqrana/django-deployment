from django.conf.urls import url
from app_four import  views


app_name='four_app'

urlpatterns=[

    url(r'^home/',views.home,name='home'),
    url(r'^other/',views.other,name='other'),
]