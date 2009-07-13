
from django import template
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.utils.encoding import smart_str
from django.template import Node, NodeList, Variable, Library
from django.template import TemplateSyntaxError, VariableDoesNotExist
from django.core.urlresolvers import reverse

from pagelets.models import Pagelet

register = template.Library()

@register.inclusion_tag('pagelets/_render_pagelet.html', takes_context=True)
def render_pagelet(context, pagelet):
    """
    Renders the named pagelet in the calling template.
    """
    if isinstance(pagelet, basestring):
        # add the slug separately because we need it in the template even
        # if this pagelet doesn't exist
        context['pagelet_slug'] = pagelet
        try:
            pagelet = Pagelet.objects.get(slug=pagelet)
        except Pagelet.DoesNotExist:
            pagelet = None
    
    if pagelet:
        # add the slug separately because we need it in the template even
        # if this pagelet doesn't exist
        context['pagelet_slug'] = pagelet.slug
        pagelet.rendered_content = pagelet.render(context)
        
    context['pagelet'] = pagelet
    return context

