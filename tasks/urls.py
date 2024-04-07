from django.urls import path, include
from . views import Task_view, Label_view, Attachment_view, Comment_view, TaskStage_view

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('task-list', Task_view, basename='task')
router.register('label', Label_view, basename='label')
router.register('attachment', Attachment_view, basename='attachment')
router.register('comment', Comment_view, basename='comment')
router.register('task-stage', TaskStage_view, basename='task-stage')

urlpatterns = [
    path('', include(router.urls))
]