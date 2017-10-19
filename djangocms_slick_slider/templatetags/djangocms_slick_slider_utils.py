from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()


@register.filter
def jsonify(dictionary, safe=True):
    dump = json.dumps(dictionary, sort_keys=True, indent=4)
    if safe:
        return mark_safe(dump)
    return dump
