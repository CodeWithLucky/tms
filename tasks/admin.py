from django.contrib import admin

# Register your models here.
from . models import Comment, Task, TaskStage, Attachment, Label

admin.site.register(Comment)
admin.site.register(Task)
admin.site.register(TaskStage)
admin.site.register(Attachment)
admin.site.register(Label)

