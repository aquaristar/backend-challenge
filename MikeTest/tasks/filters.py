from django_filters import rest_framework as filters
from .models import Task, Label


# We create filters for each field we want to be able to filter on
class TaskFilter(filters.FilterSet):
    owner__username = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ['task_id', 'title', 'description', 'task_status', 'owner__username']


class LabelFilter(filters.FilterSet):
    owner__username = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Label
        fields = ['label_id', 'name', 'owner__username']