from django.conf.urls import url
from step import views
app_name = "step"

urlpatterns = [
    url(r'^$', views.index, name='index'), 

]