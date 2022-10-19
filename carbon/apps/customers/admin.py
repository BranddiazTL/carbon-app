# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from django.contrib import admin

from .forms import CustomerAdminForm

# Carbon Stuff
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    form = CustomerAdminForm

    ordering = ("user",)

    readonly_fields = ["created_by", "modified_by", "modified"]

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user.email

        if change:
            obj.modified_by = request.user.email

        super().save_model(request, obj, form, change)
