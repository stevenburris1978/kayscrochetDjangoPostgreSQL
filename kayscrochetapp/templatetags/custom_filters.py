from django import template

register = template.Library()


@register.filter
def sum_attribute(values, attribute):
    return sum(float(value[attribute]) for value in values)
