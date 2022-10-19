# -*- coding: utf-8 -*-
import uuid
from os.path import splitext


def handle_filename(instance, filename):
    opts = instance._meta
    app_label = opts.app_label
    model_name = instance.__class__.__name__.lower()
    filename, extension = splitext(filename)
    filename = uuid.uuid4().hex
    return "{}/{}/{}/{}{}".format(
        app_label, model_name, instance.id, filename, extension
    )
