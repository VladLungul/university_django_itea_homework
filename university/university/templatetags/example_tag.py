from django import template

register = template.Library()

@register.simple_tag
def get_result_tag(arg1, arg2):
    print("----")
    return "response"
