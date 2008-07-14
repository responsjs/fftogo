from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^$', 'fftogo.views.home', name='home'),
    url(r'^legal/$', direct_to_template, {'template': 'legal.html'}, name='legal'),
    url(r'^401/$', direct_to_template, {'template': '401.html'}, name='401'),
    url(r'^403/$', direct_to_template, {'template': '403.html'}, name='403'),
    url(r'^404/$', direct_to_template, {'template': '404.html'}, name='404'),
    url(r'^500/$', direct_to_template, {'template': '500.html'}, name='500'),
    url(r'^robots.txt$', direct_to_template, {'template': 'robots.txt'}, name='robots'),
    url(r'^public/$', 'fftogo.views.public', name='public'),
    url(r'^login/$', 'fftogo.views.login', name='login'),
    url(r'^logout/$', 'fftogo.views.logout', name='logout'),
    url(r'^rooms/(?P<nickname>[\w-]+)/$', 'fftogo.views.room', name='room'),
    url(r'^rooms/$', 'fftogo.views.rooms', name='rooms'),
    url(r'^settings/$', 'fftogo.views.settings', name='settings'),
    url(r'^share/$', 'fftogo.views.share', name='share'),
    url(r'^search/$', 'fftogo.views.search', name='search'),
    url(r'^(?P<nickname>[\w-]+)/$', 'fftogo.views.user', name='user'),
    url(r'^(?P<nickname>\w+)/(?P<type>\w+)/$', 'fftogo.views.user', name='user_type'),
    url(r'^e/(?P<entry>[\w-]+)/comment/$', 'fftogo.views.entry_comment', name='entry_comment'),
    url(r'^e/(?P<entry>[\w-]+)/delete/$', 'fftogo.views.entry_delete', name='entry_delete'),
    url(r'^e/(?P<entry>[\w-]+)/undelete/$', 'fftogo.views.entry_undelete', name='entry_undelete'),
    url(r'^e/(?P<entry>[\w-]+)/c/(?P<comment>[\w-]+)/delete/$', 'fftogo.views.comment_delete', name='comment_delete'),
    url(r'^e/(?P<entry>[\w-]+)/c/(?P<comment>[\w-]+)/undelete/$', 'fftogo.views.comment_undelete', name='comment_undelete'),
    url(r'^e/(?P<entry>[\w-]+)/like/$', 'fftogo.views.entry_like', name='entry_like'),
    url(r'^e/(?P<entry>[\w-]+)/unlike/$', 'fftogo.views.entry_unlike', name='entry_unlike'),
    url(r'^e/(?P<entry>[\w-]+)/hide/$', 'fftogo.views.entry_hide', name='entry_hide'),
    url(r'^e/(?P<entry>[\w-]+)/unhide/$', 'fftogo.views.entry_unhide', name='entry_unhide'),
)
