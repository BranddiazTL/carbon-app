from urllib.parse import urljoin

from django.conf import settings

GOOGLE_PATH = settings.SYSTEM_GOOGLE_API_ENDPOINT_NAME_ROUTE_MAP


def _get_service_url(path: str) -> str:
    return urljoin(settings.SYSTEM_GOOGLE_API_HOST, path)
