from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.generics import CreateAPIView,ListAPIView

from rest_framework import authentication,permissions

from blog.serializers import UserCreationSerializer,PostSerializer

from blog.models import Post



# Create your views here.

class UserCreateView(CreateAPIView):

    serializer_class=UserCreationSerializer

class PostListCreateView(ListAPIView,CreateAPIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


