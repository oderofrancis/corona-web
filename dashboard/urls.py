from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.data_analysis,name = 'home'),
	url(r'^africa/$',views.africa,name='africa'),
	url(r'^asia/$',views.asia,name = 'asia'),
	url(r'^europe/$',views.europe,name = 'europe'),
	url(r'^south_america/$',views.south_america,name = 'south_america'),
	url(r'^north_america/$',views.north_america,name = 'north_america'),
	url(r'^oceania/$',views.oceania,name = 'oceania'),

	]