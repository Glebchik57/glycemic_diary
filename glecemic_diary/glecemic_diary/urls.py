from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from diary.views import DiaryViewSet, NoteViewSet
from users.views import PatientViewSet, GuestViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('guests', GuestViewSet)
router.register('diary', DiaryViewSet)
router.register('notes', NoteViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
