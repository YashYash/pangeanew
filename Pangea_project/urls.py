from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

admin.autodiscover()



urlpatterns = patterns('',
    url(r'^$','charity_app.views.home', name='home'),
    url(r'^charities/$', 'charity_app.views.charities', name='charities'),
    url(r'^charities/home$', 'charity_app.views.charity_home', name='charity_home'),
    url(r'^charities/new/$', 'charity_app.views.new_charity', name='new_charity'),
    url(r'^charities/info/$', 'charity_app.views.charity_info', name='charity_info'),
    url(r'^charities/videos/$', 'charity_app.views.charity_view_videos', name='view_videos'),
    url(r'^charities/newsfeed/$', 'charity_app.views.charity_newsfeed', name='view_newsfeed'),
    url(r'^charities/(?P<charity_id>\w+)/$', 'charity_app.views.view_charity', name='view_charity'),
    url(r'^charities/(?P<charity_id>\w+)/edit/$', 'charity_app.views.edit_charity', name='edit_charity'),
    url(r'^charities/(?P<charity_id>\w+)/delete/$', 'charity_app.views.delete_charity', name='delete_charity'),
    url(r'^videos/$', 'charity_app.views.videos', name='videos'),
    url(r'^videos/new/$', 'charity_app.views.new_video', name='new_video'),
    url(r'^videos/(?P<video_id>\w+)/$', 'charity_app.views.view_video', name='view_video'),
    url(r'^videos/(?P<video_id>\w+)/edit/$', 'charity_app.views.edit_video', name='edit_video'),
    url(r'^videos/(?P<video_id>\w+)/delete/$', 'charity_app.views.delete_video', name='delete_video'),
    # url(r'^signup$', 'auth_app.views.signup', name='signup'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^secret/$', 'charity_app.views.special_page', name='secret'),
    # url(r'^accounts/login$', 'auth_app.views.login1', name='login'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', 'charity_app.views.index', name='index'),

    url(r'^register/charity/$',
           RegistrationView.as_view(success_url='/charity/new/'),
           name='registration_register_charity',),

    url(r'^register/giver/$',
           RegistrationView.as_view(success_url='/giver/new/'),
           name='registration_register_giver',),

    url(r'^register/user/$',
           RegistrationView.as_view(success_url='/user/home/'),
           name='registration_register_giver',),

    url(r'^accounts/password/change/$',
            auth_views.password_change,
            name='password_change'),
    url(r'^accounts/password/change/done/$',
            auth_views.password_change_done,
            name='password_change_done'),
    url(r'^accounts/password/reset/$',
            auth_views.password_reset,
            name='password_reset'),
    url(r'^accounts/password/reset/done/$',
            auth_views.password_reset_done,
            name='password_reset_done'),
    url(r'^accounts/password/reset/complete/$',
            auth_views.password_reset_complete,
            name='password_reset_complete'),
    url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
            auth_views.password_reset_confirm,
            name='password_reset_confirm'),
    url(r'', include('registration.backends.default.urls')),
    url(r'^givers/$', 'giver_app.views.givers', name='givers'),
    url(r'^givers/new/$', 'giver_app.views.new_giver', name='new_giver'),
    url(r'^givers/profil/$', 'giver_app.views.giver_profil', name='giver_profile'),
    url(r'^givers/(?P<giver_id>\w+)/$', 'giver_app.views.view_giver', name='view_giver'),
    url(r'^givers/(?P<giver_id>\w+)/edit/$', 'giver_app.views.edit_giver', name='edit_giver'),
    url(r'^givers/(?P<giver_id>\w+)/delete/$', 'giver_app.views.delete_giver', name='delete_giver'),

)
