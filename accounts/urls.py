import views
from django.conf.urls import url

urlspatterns= [
    url (r'(?P<article_id>\d+)/add/$' , views.add , name ="add institute"),
    url (r'(?P<article_id>\d+)/edit/$' , views.edit , name ="edit institute"),
    url (r'(?P<article_id>\d+)/delete/$' , views.delete , name ="delete institute"),
    url (r'(?P<article_id>\d+)/add/$' , views.add , name ="add comments"),
    url (r'(?P<article_id>\d+)/edit/$' , views.edit , name ="edit comments"),
    url (r'(?P<article_id>\d+)/delete/$' , views.delete , name ="delete comments"),
    url (r'(?P<article_id>\d+)/add/$' , views.add , name ="add volunteer work"),
    url (r'(?P<article_id>\d+)/edit/$' , views.edit , name ="edit volunteer work"),
    url (r'(?P<article_id>\d+)/delete/$' , views.delete , name ="delete volunteer work"),
    url (r'(?P<article_id>\d+)/$' , views.show , name ="show") ,

]
