from django.urls import path
from appmusic import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('soundsurf/<int:album_id>/', views.detail, name='album_detail'),
    path('album/create/', views.album_create, name='album_create'),
    path('album/<int:album_id>/add-song/', views.add_song, name='add_song'),
    path('album/<int:album_id>/delete/', views.album_delete, name='album_delete'),
    path('song/<int:song_id>/delete/', views.song_delete, name='song_delete'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
