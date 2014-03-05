from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Pangea_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = patterns('',
    url(r'^$','charity_app.views.home', name='home'),
    url(r'^charities/$', 'charity_app.views.charities', name='charities'),
    url(r'^charities/new/$', 'charity_app.views.new_charity', name='new_charity'),
    url(r'^charities/(?P<charity_id>\w+)/$', 'charity_app.views.view_charity', name='view_charity'),
    url(r'^charities/(?P<charity_id>\w+)/edit/$', 'charity_app.views.edit_charity', name='edit_charity'),
    url(r'^charities/(?P<charity_id>\w+)/delete/$', 'charity_app.views.delete_charity', name='delete_charity'),
    url(r'^videos/$', 'charity_app.views.videos', name='videos'),
    url(r'^videos/new/$', 'charity_app.views.new_video', name='new_video'),
    url(r'^videos/(?P<video_id>\w+)/$', 'charity_app.views.view_video', name='view_video'),
    url(r'^videos/(?P<video_id>\w+)/edit/$', 'charity_app.views.edit_video', name='edit_video'),
    url(r'^videos/(?P<video_id>\w+)/delete/$', 'charity_app.views.delete_video', name='delete_video'),


)