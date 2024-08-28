from rest_framework.generics import ListCreateAPIView
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from albums.models import Album


class SongView(ListCreateAPIView):
    serializer_class = SongSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        album_id = self.kwargs.get('pk')
        return Song.objects.filter(album_id=album_id)

    def perform_create(self, serializer):
        album_id = self.kwargs.get('pk')
        album = generics.get_object_or_404(Album, pk=album_id)
        serializer.save(album=album)
