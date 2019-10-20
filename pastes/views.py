from django.shortcuts import get_object_or_404
from rest_framework import permissions, exceptions, status, generics, views, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PasteSerializer, PasteMiniSerializer
from .models import Paste

class CreatePasteView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PasteSerializer
    queryset = Paste.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.user.pk:
            serializer.save(user=request.user)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PasteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PasteSerializer
    queryset = Paste.objects.all()

class ListPasteView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PasteMiniSerializer
    queryset = Paste.objects.filter(status=Paste.PUBLIC)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['paste']
    ordering_fields = ['created']

