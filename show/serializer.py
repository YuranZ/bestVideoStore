from rest_framework.serializers import ModelSerializer
from  show.models import Video, Comment

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class CommentSerilazer(ModelSerializer):
    comment_video = VideoSerializer()
    class Meta:
        model = Comment
        fields = ("text", "date", "comment_video") #"__all__"
