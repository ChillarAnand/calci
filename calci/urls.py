from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin

from calculation.views import Calculations


admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', calculations, name='home'),
    url(r'^$', Calculations.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
