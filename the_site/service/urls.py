from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<country>[\w-]+)/$', views.api.as_view())
]