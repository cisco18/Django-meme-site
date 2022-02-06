from django import template
import os.path

register = template.Library()


def is_image_in(value):
    return os.path.exists(value)

register.filter("is_image_in",is_image_in)