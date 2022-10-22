# -*- coding: utf-8 -*-
import uuid
from os.path import splitext


def handle_filename(instance, filename):
    """
    Returns a formatted media file name adding the app, model
    and specific instance that is using the file

    :param instance: model
            the model instance of the app that is using the method
    :param filename: image
            the filename of the media file when it was uploaded
    :return: str
            the new name for the media file
    """
    opts = instance._meta
    app_label = opts.app_label
    model_name = instance.__class__.__name__.lower()
    filename, extension = splitext(filename)
    filename = uuid.uuid4().hex
    return "{}/{}/{}/{}{}".format(
        app_label, model_name, instance.id, filename, extension
    )
