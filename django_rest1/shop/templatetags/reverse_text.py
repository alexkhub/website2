from django import template

register = template.Library()


@register.filter
def reverse_text(value):
    new_value = value[:10].split('-')

    return f"{new_value[2]}.{new_value[1]}.{new_value[0]}"

@register.filter
def convert_to_int(value):
    clean_value = type(value)

    return clean_value