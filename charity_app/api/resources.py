from django.conf import settings
from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie.fields import CharField, ToOneField, ToManyField
from tastypie.resources import ModelResource, Resource
from charity_app.api.authorization import UserObjectsOnlyAuthorization
from charity_app.models import Charity, Video, ClickCount


class CharityResource(ModelResource):
    givers = ToManyField('giver_app.api.resources.GiverResource', 'givers', full=True)

    class Meta:
        queryset = Charity.objects.all()
        authentication = BasicAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        resource_name = "charity"
        allowed_methods = ['get', 'post']

class VideoResource(ModelResource):

    class Meta:
        queryset = Video.objects.all()
        resource_name = "charity"


class UserResource(ModelResource):
    charity = ToOneField(CharityResource, 'charity', full=True)
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = UserObjectsOnlyAuthorization()
        authentication = BasicAuthentication()


class ClickCountResource(ModelResource):
    video = ToOneField(VideoResource, 'video', full=True)
    user = ToOneField(UserResource, 'user', full=True)

    class Meta:
        queryset = ClickCount.objects.all()
        resource_name = "click_count"
        authorization = Authorization()
        allowed_methods = ['get', 'post']


class CharityfullResource(ModelResource):
    charity = ToOneField(CharityResource, 'charity', full=True)
    click_count = ToOneField(ClickCountResource, "click_count", full=True, null=True)

    class Meta:
        queryset = Video.objects.all()
        resource_name = "charity_full"
        authorization = Authorization()
        allowed_methods = ['get', 'post']




######################
# Non-Model Resource #
######################

class Version(object):
    def __init__(self, identifier=None):
        self.identifier = identifier


class VersionResource(Resource):
    identifier = CharField(attribute='identifier')

    class Meta:
        resource_name = 'version'
        allowed_methods = ['get']
        object_class = Version
        include_resource_uri = False

    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.identifier
        else:
            kwargs['pk'] = bundle_or_obj['identifier']

        return kwargs

    def get_object_list(self, bundle, **kwargs):
        return [Version(identifier=settings.VERSION)]

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle, **kwargs)