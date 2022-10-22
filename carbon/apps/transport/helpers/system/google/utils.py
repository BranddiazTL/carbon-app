# -*- coding: utf-8 -*-
from urllib.parse import urljoin

from django.conf import settings

GOOGLE_PATH = settings.SYSTEM_GOOGLE_API_ENDPOINT_NAME_ROUTE_MAP


def _get_service_url(path: str) -> str:
    """
    Returns the specific url related to the system (Google)
    along side with the endpoint path to complete the request

    :param path: str
        the endpoint path for the request
    :return: str
        request full url + path
    """
    return urljoin(settings.SYSTEM_GOOGLE_API_HOST, path)
