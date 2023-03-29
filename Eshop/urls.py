from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings

admin.site.site_header = "Anupam Admin"
admin.site.site_title = "Anupam Admin Portal"
admin.site.index_title = "Welcome to Anupam's Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
