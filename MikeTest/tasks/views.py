from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Task, Label
from .permissions import IsOwnerOrReadOnly
from .serializers import TaskSerializer, LabelSerializer
from .filters import TaskFilter, LabelFilter


class ListCreateTaskAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    #pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TaskFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyTaskAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]



class ListCreateLabelAPIView(ListCreateAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
    permission_classes = [IsAuthenticated]
    #pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LabelFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyLabelAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]