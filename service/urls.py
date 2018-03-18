from django.conf.urls import url

from . import views

urlpatterns = [
	#url(r'^api/(?P<country>[\w-]+)/$', views.api.as_view()),
	url(r'(?P<country>[\w-]+)/$', views.web.as_view(), name='details'),
url(r'home',views.index.as_view()),
]