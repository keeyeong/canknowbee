from django import template

register = template.Library()


@register.filter
def index(source_list, i):
    return source_list[int(i) - 1]
