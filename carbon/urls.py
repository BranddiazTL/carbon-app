# -*- coding: utf-8 -*-
"""carbon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Third Party Stuff
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views import defaults as dj_default_views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

# Carbon Stuff
from carbon.apps.base import views as base_views
from carbon.apps.customers import views
from carbon.apps.transport.views import TransportViewSet

handler500 = base_views.server_error

# Carbon API routes
router = routers.DefaultRouter()
router.register(r"api/customers", views.CustomerViewSet)
router.register(r"api/transport", TransportViewSet, basename="transport")

# Wire up our API using automatic URL routing.

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", auth_views.obtain_auth_token),
    path("", include(router.urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/docs/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]


if settings.DEBUG:
    urlpatterns += [
        url(
            r"^400/$",
            dj_default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        url(
            r"^403/$",
            dj_default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied!")},
        ),
        url(
            r"^404/$",
            dj_default_views.page_not_found,
            kwargs={"exception": Exception("Not Found!")},
        ),
        url(r"^500/$", handler500),
    ]
