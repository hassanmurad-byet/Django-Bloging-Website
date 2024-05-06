from django import template

register = template.Library()


def renge_filter(value):
    return value[0:500]+ "...................."

register.filter('range_filter', renge_filter)