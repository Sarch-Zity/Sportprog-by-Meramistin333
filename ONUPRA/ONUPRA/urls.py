from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.shortcuts import render
from django.views.generic.base import RedirectView

# Обработчик ошибки 404
def handler404(request, exception):
    return render(request, 'error404.html', status=404)

# Обработчик ошибки 500
def handler500(request):
    return render(request, 'error500.html', status=500)

# Обработчик ошибки 403
def csrf_failure(request, reason=""):
    return render(request, 'error403.html', status=403)

urlpatterns = [
    path('2355admin/', admin.site.urls),
    path('', include('main.urls')),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/ONUPRA/icons/favicon2.ico', permanent=True))
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]
# else:
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
#         re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
#         ]

handler404 = handler404
handler500 = handler500