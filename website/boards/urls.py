from django.urls import path
from boards import views


urlpatterns = [
    path('',views.show,name="show"),
    #path('/new_topic',views.new_topic,name="new_topic"),


]