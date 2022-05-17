from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PhotoListView,
    PhotoDetailView,
    TagPhotoListView,
    PhotoCreateView,
)

urlpatterns = [
    path("", PhotoListView.as_view(), name="photo-list"),
    path("tag/<str:tag>/", TagPhotoListView.as_view(), name="tag-photo"),
    path("photo/<int:pk>", PhotoDetailView.as_view(), name="photo-detail"),
    path("create/", PhotoCreateView.as_view(), name="photo-create"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
