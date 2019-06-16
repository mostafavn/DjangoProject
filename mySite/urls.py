from django.contrib import admin
from django.urls import path, include
from fa import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('fa/', include('fa.urls')),
    path('en/', include('en.urls')),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('', RedirectView.as_view(url='/fa/', permanent=True)),
]

handler404 = views.error
handler500 = views.error
handler403 = views.error
handler400 = views.error
