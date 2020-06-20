from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video, Comment
from show.serializer import CommentSerilazer, VideoSerializer
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from json import dumps

class UpdateDestroyVideo(RetrieveUpdateAPIView):
    serializer_class = VideoSerializer
    queryset =  Video.objects.all()


class VideoList(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class CommentList(ListAPIView):
    serializer_class = CommentSerilazer
    queryset = Comment.objects.all()

class CreatVideo(CreateAPIView):
    serializer_class = VideoSerializer


def hello(request):
    return HttpResponse("<h1>hello world</h1>")


def world(request):
    response = {"name":"Bogdan", "d":34, "arr":[1,2,3,4,5]}
    response["content"] = Video.objects.all()
    return render(request, "index.html", response)


def accept_comment(request, id):
    Comment.objects.create(text=request.POST["com"], comment_video_id=id)
    print(request.POST["pwd"])
    return redirect("main_page")


def one_video(request, id):
    response = {"video":Video.objects.get(id=id)}
    return render(request, "one_video.html", response)

def ajax_like(request):
    id = request.GET["id"]
    video = Video.objects.get(id=id)
    video.likes += 1
    video.save()
    print(request.GET["id"])
    return HttpResponse(video.likes)

def ajax_comment(request):
    id = request.GET["id"]
    val = request.GET["val"]
    com = Comment.objects.create(text=val, comment_video_id=id)
    response = {"id":com.id, "date":str(com.date)}
    response = dumps(response)
    return HttpResponse(response)