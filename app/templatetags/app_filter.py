from django import template

register = template.Library()

@register.filter
def get_range(number):
    return range(number)

@register.filter
def sub(num1, num2):
    return num1 - num2