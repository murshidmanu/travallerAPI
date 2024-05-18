from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from places.models import Place, Gellery, Comment


class PlaceSerializer(ModelSerializer):
    likes = serializers.SerializerMethodField()
    is_likes = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ("id", "name", "featured_image", "location", "likes", "is_likes")  
    def get_likes(self, instance):
        return instance.likes.count()

    def get_is_likes(self, instance):  
        request = self.context.get("request")
        if instance.likes.filter(username=request.user.username).exists():
            return True
        else:
            return False



class GellerySerializer(ModelSerializer):
    class Meta:
        fields = ("id", "featured_image" )
        model = Gellery



class PlaceDetailSerializer(ModelSerializer):

    category = serializers.SerializerMethodField()
    gellery = serializers.SerializerMethodField()

    class Meta:
        fields = ("id", "name", "featured_image", "location", "description", "category", "gellery")
        model = Place

    def get_category(self, instance):
        return instance.category.name
    
    def get_gellery(self, instance):
        request = self.context.get("request")
        featured_image = Gellery.objects.filter(place=instance)
        serializer = GellerySerializer(featured_image, many=True,context={"request":request})
        return serializer.data


class CommentSerializer(ModelSerializer):
    replies = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    class Meta:
        fields = ("id", "user", "comment", "date", "replies")
        model = Comment

    def get_user(self, instance):
        return instance.user.username
    
    def get_replies(self, instance):
        instances = Comment.objects.filter(parent_comment=instance)
        serializer = CommentSerializer(instances, many=True)
        return serializer.data
    
    def get_date(self, instance):
        return instance.date.strftime("%d %B %Y")

