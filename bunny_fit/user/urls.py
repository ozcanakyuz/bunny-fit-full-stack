from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("userprofile", views.index, name="user_profile"),
    # path("update/<int:id>", views.user_posts_update, name="user_post_update"),
    # path('settings/', views.user_settings, name='user_settings'),
    # path('password/', views.user_password, name='user_password'),
]