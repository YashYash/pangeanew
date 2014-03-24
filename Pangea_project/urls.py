from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from tastypie.api import Api
from charity_app.api.resources import CharityResource, UserResource, VersionResource, CharityfullResource, ClickCountResource
from giver_app.api.resources import GiverResource, GiverfullResource

admin.autodiscover()

# api urls
v1_api = Api(api_name="v1")
v1_api.register(CharityResource())
v1_api.register(GiverResource())
v1_api.register(CharityfullResource())
v1_api.register(GiverfullResource())
v1_api.register(UserResource())
v1_api.register(VersionResource())
v1_api.register(ClickCountResource())


urlpatterns = patterns('',
    # Social Auth in settings.py
    url('', include('social.apps.django_app.urls', namespace='social')),

    # index.html, home page. In charity app
    url(r'^$', 'charity_app.views.index', name='index'),

    # Charities in charity app
    url(r'^$','charity_app.views.home', name='home'),
    url(r'^loginall$','charity_app.views.logs', name='logs'),
    url(r'^charities/$', 'charity_app.views.charities', name='charities'),
    url(r'^charities/home$', 'charity_app.views.charity_home', name='charity_home'),
    url(r'^charities/new/$', 'charity_app.views.new_charity', name='new_charity'),
    url(r'^charities/info/$', 'charity_app.views.charity_info', name='charity_info'),
    url(r'^charities/videos/$', 'charity_app.views.charity_view_videos', name='view_videos'),
    url(r'^charities/newsfeed/$', 'charity_app.views.charity_newsfeed', name='view_newsfeed'),
    url(r'^charities/(?P<charity_id>\w+)/$', 'charity_app.views.view_charity', name='view_charity'),
    url(r'^charities/(?P<charity_id>\w+)/edit/$', 'charity_app.views.edit_charity', name='edit_charity'),
    url(r'^charities/(?P<charity_id>\w+)/delete/$', 'charity_app.views.delete_charity', name='delete_charity'),

    #fb charities
    url(r'^fbcharities/$', 'charity_app.views.fbcharities', name='fbcharities'),
    url(r'^fbcharities/home$', 'charity_app.views.fbcharity_home', name='fbcharity_home'),
    url(r'^fbcharities/new/$', 'charity_app.views.fbnew_charity', name='fbnew_charity'),
    url(r'^fbcharities/info/$', 'charity_app.views.fbcharity_info', name='fbcharity_info'),
    url(r'^fbcharities/(?P<fbcharity_id>\w+)/$', 'charity_app.views.fbview_charity', name='fbview_charity'),
    url(r'^fbcharities/(?P<fbcharity_id>\w+)/edit/$', 'charity_app.views.fbedit_charity', name='fbedit_charity'),
    url(r'^fbcharities/(?P<fbcharity_id>\w+)/delete/$', 'charity_app.views.fbdelete_charity', name='fbdelete_charity'),

    # Videos in charity_app
    url(r'^videos/$', 'charity_app.views.videos', name='videos'),
    url(r'^videos/new/$', 'charity_app.views.new_video', name='new_video'),
    url(r'^videos/(?P<video_id>\w+)/$', 'charity_app.views.view_video', name='view_video'),
    url(r'^videos/(?P<video_id>\w+)/edit/$', 'charity_app.views.edit_video', name='edit_video'),
    url(r'^videos/(?P<video_id>\w+)/delete/$', 'charity_app.views.delete_video', name='delete_video'),



    # Users in user_app
    url(r'^users/$', 'user_app.views.users', name='users'),
    url(r'^users/add_profile/$', 'user_app.views.addprofile', name='add_profile'),
    url(r'^users/newsfeed/$', 'user_app.views.newsfeed', name='newsfeed'),
    url(r'^users/home/$', 'user_app.views.users_home', name='users_home'),
    url(r'^users/new/$', 'user_app.views.new_user', name='new_user'),
    url(r'^users/profile/$', 'user_app.views.user_profile', name='user_profile'),
    url(r'^users/(?P<user_id>\w+)/$', 'user_app.views.view_user', name='view_user'),
    url(r'^users/(?P<user_id>\w+)/edit/$', 'user_app.views.edit_user', name='edit_user'),
    url(r'^users/(?P<user_id>\w+)/delete/$', 'user_app.views.delete_user', name='delete_user'),

    # fbUsers in user_app
    url(r'^fbusers/$', 'user_app.views.fbusers', name='fbusers'),
    url(r'^fbusers/add_profile/$', 'user_app.views.fbaddprofile', name='fbadd_profile'),
    url(r'^fbusers/newsfeed/$', 'user_app.views.fbnewsfeed', name='fbnewsfeed'),
    url(r'^fbusers/home/$', 'user_app.views.fbusers_home', name='fbusers_home'),
    url(r'^fbusers/profile/$', 'user_app.views.fbuser_profile', name='fbuser_profile'),


    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Django Auth
    url(r'^accounts/', include('registration.backends.default.urls')),

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

    # givers
    url(r'^givers/$', 'giver_app.views.givers', name='givers'),
    url(r'^givers/stripe/$', 'giver_app.views.stripe', name='stripe'),
    url(r'^givers/new/$', 'giver_app.views.new_giver', name='new_giver'),
    url(r'^givers/profil/$', 'giver_app.views.giver_profil', name='giver_profile'),
    url(r'^givers/info/$', 'giver_app.views.giver_info', name='giver_info'),
    url(r'^givers/(?P<giver_id>\w+)/$', 'giver_app.views.view_giver', name='view_giver'),
    url(r'^givers/(?P<giver_id>\w+)/edit/$', 'giver_app.views.edit_giver', name='edit_giver'),
    url(r'^givers/(?P<giver_id>\w+)/delete/$', 'giver_app.views.delete_giver', name='delete_giver'),
    url(r'^givers/page/$', 'giver_app.views.giver_page', name='giver_page'),

    #fb givers

    url(r'^fbgivers/$', 'giver_app.views.fbgivers', name='fbgivers'),
    url(r'^fbgivers/stripe/$', 'giver_app.views.fbstripe', name='fbstripe'),
    url(r'^fbgivers/new/$', 'giver_app.views.fbnew_giver', name='fbnew_giver'),
    url(r'^fbgivers/profil/$', 'giver_app.views.fbgiver_profil', name='fbgiver_profile'),
    url(r'^fbgivers/info/$', 'giver_app.views.fbgiver_info', name='fbgiver_info'),
    url(r'^fbgivers/(?P<fbgiver_id>\w+)/$', 'giver_app.views.fbview_giver', name='fbview_giver'),
    url(r'^fbgivers/(?P<fbgiver_id>\w+)/edit/$', 'giver_app.views.fbedit_giver', name='fbedit_giver'),
    url(r'^fbgivers/(?P<fbgiver_id>\w+)/delete/$', 'giver_app.views.fbdelete_giver', name='fbdelete_giver'),
    url(r'^fbgivers/page/$', 'giver_app.views.giver_page', name='fbgiver_page'),

    #Stripe payment
    url(r'^payment/$', 'charity_app.views.payment', name='payment'),
    url(r'^api/', include(v1_api.urls)),

    #angular Micro donation video page
    url(r'^stream_videos/$', 'charity_app.views.angular', name="stream"),
    url(r'^fbstream_videos/$', 'charity_app.views.fbangular', name="fbstream"),

    #api and tastypie
    url(r'api/lecture/doc/',
        include('tastypie_swagger.urls', namespace='tastypie_swagger'),
        kwargs={"tastypie_api_module": "v1_api",
                "namespace": "charity_app_tastypie_swagger"},
    ),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{
        'document_root': settings.MEDIA_ROOT}))

