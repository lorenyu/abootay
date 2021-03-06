from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from config import staticfiles
admin.autodiscover()

urlpatterns = patterns('',
    ('^$', 'game.views.index'),
    ('^play$', 'game.views.play'),

    # Example:
    # (r'^abootay/', include('abootay.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    # (r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    
    # static files (for development environment only. On production, nginx has its own rules)
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': staticfiles.path() })
)
