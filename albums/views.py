from rest_framework.generics import ListCreateAPIView
from .models import Album
from .serializers import AlbumSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AlbumView(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
