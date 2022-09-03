
from django.urls import re_path, include
from django.contrib import admin
from . import views
from django.conf import settings

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.HomePage.as_view(), name='home'),
    re_path(r'accounts/', include('accounts.urls', namespace='accounts')),
    re_path(r'accounts/', include('django.contrib.auth.urls')),
    re_path(r'^test/$', views.TestPage.as_view(), name = 'test'),
    re_path(r'^thanks/$', views.ThanksPage.as_view(), name = 'thanks'),
    re_path(r'^posts/', include('posts.urls', namespace='posts')),
    re_path(r'^groups/', include('groups.urls', namespace='groups')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    re_path(r'^__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
