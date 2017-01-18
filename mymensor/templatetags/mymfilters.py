from django import template

register = template.Library()

@register.filter(name="lookupvpnumber")
def lookupvpnumber(value, key):
    try:
        return value[key]
    except:
        return key