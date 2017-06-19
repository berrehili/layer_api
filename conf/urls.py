from django.conf.urls import patterns, include, url
from layer_api import views
from rest_framework import viewsets, routers

urlpatterns = patterns('',
    # Registration of new users
    url(r'^register/$', views.RegistrationView.as_view()),
    url(r'^login/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^update/', views.UpdateUserView.as_view()),
    # url(r'^user/(?P<user_id>[0-9]*)$', views.UserInfosView.as_view()),

    # Todos endpoint
    # url(r'^todos/$', views.TodosView.as_view()),
    # url(r'^todos/(?P<todo_id>[0-9]*)$', views.TodosView.as_view()),

    # # API authentication
    # url(r'^api-auth/', include('rest_framework.urls',\
    #     namespace='rest_framework')),
)

