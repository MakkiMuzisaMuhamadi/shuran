
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_title = 'Shuran'
admin.site.index_title = 'Welcome to Shuran Admin Panel'
admin.site.site_header = 'Shuran'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)