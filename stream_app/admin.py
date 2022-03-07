from django.contrib import admin
from stream_app.models import StreamPlatform, WatchList, Review

# Register your models here.
admin.site.register(StreamPlatform)
admin.site.register(WatchList)
admin.site.register(Review)