from django.urls import path
from . import views #added
urlpatterns = [ 
    path ("", views.index, name="index"),
    path ("<int:month>", views.monthly_challenge_by_number),
    path ("<str:month>", views.monthly_challenge, name="month-challenge")
 ] #here, <month> is a placeholder.