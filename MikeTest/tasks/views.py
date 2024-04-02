from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Task, Label
from .permissions import IsOwnerOrReadOnly
from .serializers import TaskSerializer, LabelSerializer
from .filters import TaskFilter, LabelFilter


class ListCreateTaskAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TaskFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)        


class RetrieveUpdateDestroyTaskAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class ListCreateLabelAPIView(ListCreateAPIView):
    serializer_class = LabelSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LabelFilter

    def perform_create(self, serializer):        
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Label.objects.filter(owner=self.request.user)


class RetrieveUpdateDestroyLabelAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LabelSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        return Label.objects.filter(owner=self.request.user)