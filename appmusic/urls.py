from django.urls import path
from appmusic import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('soundsurf/<int:album_id>/', views.detail, name='album_detail'),
    path('album/create/', views.album_create, name='album_create'),
    path('album/<int:album_id>/add-song/', views.add_song, name='add_song'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
