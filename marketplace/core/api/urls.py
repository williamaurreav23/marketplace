# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from marketplace.athletes.api.v1.views import AthleteRegistrationView
from marketplace.athletes.api.v1.viewsets import AthleteViewSet
from marketplace.supporters.api.v1.views import SupporterRegistrationView


router_v1 = routers.DefaultRouter()

router_v1.register('athletes', AthleteViewSet, 'athletes')

app_name = 'api'
urlpatterns = [
    # Obtaining a token. Security
    url(r'^v1/register/athletes', AthleteRegistrationView.as_view(), name='register_athletes'),
    url(r'^v1/register/supporters', SupporterRegistrationView.as_view(), name='register_supporters'),
    url(r'^v1/login/', obtain_jwt_token),
    url(r'^v1/refresh/', refresh_jwt_token),
    url(r'^v1/', include((router_v1.urls, 'v1'), namespace='v1'))
]


