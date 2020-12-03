from django.conf.urls import url
from userapp import views

urlpatterns = [
    url(r'^api/get_all_users$', views.get_all_users),
    url(r'^api/get_user/(?P<pk>[0-9]+)$', views.get_user),
    url(r'^api/create_user', views.create_user)
]
