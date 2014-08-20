from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup


register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def html2js(value):
    soup = mark_safe(BeautifulSoup(value))
    return repr(soup)

register.filter('h2j', html2js)

@register.tag('htmltojs')
def htmltojs(parser, token):
    nodelist = parser.parse(('endhtmltojs',))
    parser.delete_first_token()
    return HtmlToJs(nodelist)

class HtmlToJs(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        output = self.nodelist.render(context)
        return html2js(output)