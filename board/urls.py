from django.urls import path
from .views import (
    PostView,
    PostDetailView,
)

urlpatterns = [
    path('', PostView.as_view()),
    path('/<int:postid>', PostDetailView.as_view())
]
