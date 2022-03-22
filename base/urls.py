from django.urls import path
from .views import (
    login_page,
    logout_user,
    signup_page,
    home,
    room,
    create_room,
    update_room,
    delete_room,
    delete_message,
    topics_page,
    activity_page
)

urlpatterns = [
    path('login/', login_page, name="login"),
    path('logout/', logout_user, name="logout"),
    path('signup/', signup_page, name="signup"),
    
    path('', home, name="home"),
    
    path('room/<str:pk>/', room, name="room"),
    path('create-room/', create_room, name="create-room"),
    path('update-room/<str:pk>/', update_room, name="update-room"),
    path('delete-room/<str:pk>/', delete_room, name="delete-room"),
    path('delete-message/<str:pk>/', delete_message, name="delete-message"),
    
    path('topics/', topics_page, name="topics"),
    path('activity/', activity_page, name="activity"),
]
