from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet, basename='post-list')
router.register(r'groups', GroupViewSet, basename='group-list')
router.register(r'posts\/(?P<post_id>[0-9]*)\/comments',
                CommentViewSet,
                basename='comment-list'
                )
router.register(r'follow', FollowViewSet, basename='follow-list')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
