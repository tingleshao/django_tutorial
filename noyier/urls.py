from django.conf.urls.defaults import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noyier.views.home', name='home'),
    # url(r'^noyier/', include('noyier.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	(r'^contacts/', 'contacts.views.show_contacts'),
	(r'^news/$', 'news.views.index'),
	(r'^news/(?P<news_id>\d+)/$','news.views.detail'),
	(r'^admin/', include(admin.site.urls)),
	(r'^profile/', 'siteprofile.views.welcome'),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),

)