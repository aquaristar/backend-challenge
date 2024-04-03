from django.db import models

TASK_STATUS=(
    ("o", "Open"),
    ("i", "In progress"),
    ("h", "Inpeded"),
    ("c", "Completed"),
)


class Label(models.Model):
    label_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey('auth.User', related_name='labels', on_delete=models.CASCADE)    
    
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    task_status = models.CharField(max_length=9,
                                   choices=TASK_STATUS,
                                   blank=False,
                                   default="o",
                                   help_text="Current status of the task")
    labels = models.ManyToManyField(Label)
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["title"]
    
    def __str__(self):
        return self.title
    