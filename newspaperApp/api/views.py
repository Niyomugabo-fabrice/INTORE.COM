from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def UserApi(request, id=None):
    if request.method == 'GET':
        if id:
            try:
                user = User.objects.get(pk=id)
                serializer = UserSerializer(user)
            except User.DoesNotExist:
                return Response({"Error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response({"Error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            user = User.objects.get(pk=id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"Error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ArticleApi(request, id=None):
    if request.method == 'GET':
        if id:
            try:
                article = Articles.objects.get(pk=id)
                serializer = ArticlesSerializer(article)
            except Articles.DoesNotExist:
                return Response({"Error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            articles = Articles.objects.all()
            serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            article = Articles.objects.get(pk=id)
        except Articles.DoesNotExist:
            return Response({"Error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ArticlesSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            article = Articles.objects.get(pk=id)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Articles.DoesNotExist:
            return Response({"Error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def AuthorApi(request, id=None):
    if request.method == 'GET':
        if id:
            try:
                author = Authors.objects.get(pk=id)
                serializer = AuthorSerializer(author)
            except Authors.DoesNotExist:
                return Response({"Error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            authors = Authors.objects.all()
            serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            author = Authors.objects.get(pk=id)
        except Authors.DoesNotExist:
            return Response({"Error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            author = Authors.objects.get(pk=id)
            author.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Authors.DoesNotExist:
            return Response({"Error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def CommentApi(request, id=None):
    if request.method == 'GET':
        if id:
            try:
                comment = Comments.objects.get(pk=id)
                serializer = CommentSerializer(comment)
            except Comments.DoesNotExist:
                return Response({"Error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            comments = Comments.objects.all()
            serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            comment = Comments.objects.get(pk=id)
        except Comments.DoesNotExist:
            return Response({"Error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            comment = Comments.objects.get(pk=id)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comments.DoesNotExist:
            return Response({"Error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
