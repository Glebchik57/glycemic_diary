from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from glecemic_diary.diary.views import DiaryViewSet, NoteViewSet
from glecemic_diary.users.views import PatientViewSet, GuestViewSet

router = DefaultRouter()
router.registry('patients', PatientViewSet)
router.registry('guests', GuestViewSet)
router.registry('diary', DiaryViewSet)
router.registry('notes', NoteViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
