from . import views
from django.urls import path

#name spacing
app_name='movieapp'

urlpatterns = [
    path('',views.index,name="index"),
    path('movie/<int:movie_id>', views.details,name='details'),
    path('add/',views.add_movie,name="add_movie"),
    path('update/<int:id>/',views.update_fn,name="update_fn"),
    path('delete/<int:id>/',views.delete,name="delete"),
    ]
