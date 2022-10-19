# Third Party Stuff
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Carbon Stuff
from carbon.apps.base.models import TimeStampedUUIDModel
from carbon.apps.base.utils.media_filename import handle_filename


class Customer(TimeStampedUUIDModel):
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"

    status_choices = (
        (SUSPENDED, SUSPENDED),
        (ACTIVE, ACTIVE),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=False,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        "Image", upload_to=handle_filename, max_length=500, blank=False
    )
    status = models.CharField(
        "Customer Status",
        blank=True,
        null=True,
        choices=status_choices,
        max_length=20,
        default=ACTIVE,
    )
    home_address = models.CharField("Home Address", max_length=256)
    work_address = models.CharField(
        "Work Address", blank=True, null=True, max_length=256
    )
    city = models.CharField("Address City", max_length=256)

    # Auto populated fields
    created_by = models.CharField("Created by", max_length=256)
    modified_by = models.CharField("Modified by", blank=True, null=True, max_length=256)

    class Meta:
        verbose_name = _("customer")
        verbose_name_plural = _("customers")
        ordering = ("-created",)

    def __str__(self):
        return self.user.email
