import views
from django.conf.urls import url


    url(r'^$', views.girls2),
    url(r'^hi/$', views.girls3),
    url (r'(?P<article_id>\d+)/$' , views.show , name ="show") ,
    url (r'^list$', views.list) ,
     url (r'^survey$', views.survey) ,
]
