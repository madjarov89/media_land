from django import template

register = template.Library()


@register.filter
def placeholder(input_value, token):
    input_value.field.widget.attrs['placeholder'] = token
    return input_value


@register.filter
def form_class(element, class_name):
    default_class = element.field.widget.attrs.get('class', '')
    element.field.widget.attrs['class'] = default_class + ' ' + class_name
    return element
