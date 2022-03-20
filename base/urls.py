from django.urls import path
from .views import login_page, logout_user, signup_page, home, room, create_room, update_room, delete_room, topics_page

urlpatterns = [
    path('login/', login_page, name="login"),
    path('logout/', logout_user, name="logout"),
    path('signup/', signup_page, name="signup"),
    
    path('', home, name="home"),
    
    path('room/<str:pk>/', room, name="room"),
    path('create-room/', create_room, name="create-room"),
    path('update-room/<str:pk>/', update_room, name="update-room"),
    path('delete-room/<str:pk>/', delete_room, name="delete-room"),
    
    path('topics/', topics_page, name="topics"),
]
