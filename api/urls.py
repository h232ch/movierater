from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.views import MovieViewSet, RatingViewSet, UserViewSet, \
    BoardCommentSet, MovieListViewSet, \
    DogViewSet, RuleViewSet, CustomObtainAuthToken, example_view

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('movielist', MovieListViewSet)
router.register('ratings', RatingViewSet)
router.register('users', UserViewSet)
router.register('comments', BoardCommentSet)
router.register('dog', DogViewSet)
router.register('rule', RuleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', CustomObtainAuthToken.as_view(),
         name='token_obtain_pair'),
    # JWT Settings
    path('example/', example_view, name='example-view'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
