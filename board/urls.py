from django.urls import path
from .views import (
    PostView,
    PostDetailView,
    ReplyView,
    ReplyDetailView
)

urlpatterns = [
    path('', PostView.as_view()),
    path('/<int:postid>', PostDetailView.as_view()),
    path('/<int:postid>/reply', ReplyView.as_view()),
    path('/reply/<int:replyid>', ReplyDetailView.as_view())
]
