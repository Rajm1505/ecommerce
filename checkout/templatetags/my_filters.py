from django.template import Library

register = Library()

@register.filter
def deliveryCharges(value):
    if int(value) > 499:
        return "FREE"
    else:
        return 50

@register.filter
def total(value,args):
    # print(args)
    if args != "FREE":
        return value+int(args)
    return value
