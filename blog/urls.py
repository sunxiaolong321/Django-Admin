from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # path('api/index/', views.IndexPostListAPIView.as_view())
    path('api/index/', index),
]
