from django.urls import path
from .views import UserApi, ArticleApi, AuthorApi, CommentApi

urlpatterns = [
    path('user/', UserApi, name='All_users'),
    path('user/<int:id>/', UserApi, name='users'),
    path('article/', ArticleApi, name="All_articles"),
    path('article/<int:id>/', ArticleApi, name="ArticleApi"),
    path('author/', AuthorApi, name="All_authors"),
    path('author/<int:id>/', AuthorApi, name="AuthorApi"),
    path('comment/', CommentApi, name="All_comments"),
    path('comment/<int:id>/', CommentApi, name="CommentApi"),
]
