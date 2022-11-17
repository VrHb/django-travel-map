from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from where_to_go import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_main),
    path('places/<int:place_id>', views.show_place)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
