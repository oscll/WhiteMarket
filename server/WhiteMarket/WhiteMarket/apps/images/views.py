from WhiteMarket.apps.images.serializers import ImageSerializer
from WhiteMarket.apps.images.models import Image
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from rest_framework import permissions
from WhiteMarket import custompermission

class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    name = 'image-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        )
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    name = 'image-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
        )
