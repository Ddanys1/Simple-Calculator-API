from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,),
	path('set/',views.home,),
	path('get',views.ipaddress),
	path('answer',views.answer),
	path('list',views.check_list),
	]