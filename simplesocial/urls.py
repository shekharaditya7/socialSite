
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'accounts/', include('accounts.urls', namespace='accounts')),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^test/$', views.TestPage.as_view(), name = 'test'),
    url(r'^thanks/$', views.ThanksPage.as_view(), name = 'thanks'),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^groups/', include('groups.urls', namespace='groups')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    url(r'^__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
