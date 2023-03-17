from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', include('register.urls')),
    path('', include('mainpage.urls')),
    path('createnew/', include('news.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
