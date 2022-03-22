from django.urls import path
from .views import (
    login_page,
    logout_user,
    signup_page,
    user_profile,
    update_user,
    home,
    room,
    topics_page,
    activity_page,
    create_room,
    update_room,
    delete_room,
    delete_message
)

urlpatterns = [
    path('login/', login_page, name="login"),
    path('logout/', logout_user, name="logout"),
    path('signup/', signup_page, name="signup"),
    
    path('profile/<str:pk>/', user_profile, name="user-profile"),
    path('update-user/', update_user, name="update-user"),
    
    path('', home, name="home"),
    path('topics/', topics_page, name="topics"),
    path('activity/', activity_page, name="activity"),
    
    path('room/<str:pk>/', room, name="room"),
    path('create-room/', create_room, name="create-room"),
    path('update-room/<str:pk>/', update_room, name="update-room"),
    path('delete-room/<str:pk>/', delete_room, name="delete-room"),
    path('delete-message/<str:pk>/', delete_message, name="delete-message"),
]
