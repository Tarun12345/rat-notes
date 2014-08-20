import markdown2
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def markdown2_filter(value):
    return mark_safe(markdown2.markdown(force_text(value)))

from django.utils import simplejson
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def as_json(data):
    return mark_safe(simplejson.dumps(data))

register.filter('markdown', markdown2_filter)

