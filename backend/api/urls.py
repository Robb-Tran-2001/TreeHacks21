from django.urls import path
from .views import UserView, ImageView, CreateImageView, CreateUserView, LoginUserView
from django.conf import settings
from django.conf.urls.static import static

#Endpoints to call views in views.py to handle requests
urlpatterns = [
    #matches path to the functions in views.py
    path('users', UserView.as_view()),
    path('images', ImageView.as_view()),
    path('signup', CreateUserView.as_view()),
    path('login', LoginUserView.as_view()),
    path('upload', CreateImageView.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)