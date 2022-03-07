from django.urls import path
from stream_app.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV,ReviewList, ReviewDetail,ReviewCreate

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-name'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-name'),
    #path('review/', ReviewList.as_view(), name='review-list'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('review/<int:pk>',ReviewDetail.as_view(), name='review-detail'), 
]
