from django import template

register = template.Library()


@register.filter
def index_minus_one(source_list, i):
    """Returns the item at i-1 from source_list"""
    return source_list[int(i) - 1]
