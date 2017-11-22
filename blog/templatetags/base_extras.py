from django import template
from django.core.urlresolvers import reverse, resolve
from urllib import urlencode

from blog.avatar.identicon import Avatar as Identicon

import base64


register = template.Library()

@register.simple_tag
def is_active(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return "active"
    return ""

@register.simple_tag
def is_active_with_querystr(request, url):
    url_name =  urlencode(request.GET)
    if url_name == url:
        return "active"
    return ""
    # url_name = resolve(request.path).url_name
    # print url_name, url
    # if url_name == url:
    #     return "active"
    # return ""

@register.filter(name='lineup')
def lineup(ls):
    return ', '.join(ls[:-1])+' and '+ls[-1] if len(ls)>1 else ls[0]

@register.filter(name='avatar')
def avatar(email):
    avatar = Identicon(rows=10, columns=10)
    image = avatar.get_image(seed=str(email), width=22, height=22, pad=3)
    return "data:image/png;base64,{}".format(base64.b64encode(image))

