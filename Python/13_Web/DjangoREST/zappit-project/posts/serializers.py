from rest_framework import serializers
from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')  # Modify how to return data fields in JSON
    poster_id = serializers.ReadOnlyField(source='poster.id')
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster',
                  'poster_id', 'created', 'votes']  # Column names from Post model

    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']
