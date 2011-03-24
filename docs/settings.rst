List of Available Settngs
=================================

PAGELET_TEMPLATE_TAGS
-------------------------

Default: `[]`

This setting also you to specify a list of template tags to include when rendering
pagelet content. The names of the template tag libraries should be given as strings
`pagelet_tags` are defined and available when rendering pagelet content. 


PAGELET_BASE_TEMPLATES
-------------------------

Default: `[]`

By default pages all render using the `pagelets/view_page.html` template. If you wish
to define additional templates which pages can use then you can define them here. This
should be a list of tuples i.e. `[("pagelets/two_col_page.html", "Two Column Template"), ]`.


PAGELET_CONTENT_AREAS
-------------------------

Default: `(('main', 'Main'), )`

Pagelets use content areas to define when they render on a given page. The default
`pagelets/view_page.html` only uses one content area called `main`. If you define additional
content areas in your page templates then need to add them into the choices using
this setting.


PAGELET_CONTENT_TYPES
-------------------------

Default: `{}`

Pagelets content can be one of three types by default: HTML, Markdown, and Textile. Using
this setting you can define additional content types or override the behavior of the default
types. This setting should be a nested dictionary. The first set of keys is the content type.
For each content type defined the value dictionary should contain a verbose label for this content
type and a render function. This render function is called on the template compiled pagelet
content to convert it to HTML. See the built-in content types for a reference::

    CONTENT_HTML = 'html'
    CONTENT_MARKDOWN = 'markdown'
    CONTENT_TEXTILE = 'textile'

    BUILTIN_CONTENT_TYPES = {
        CONTENT_HTML: {
            'label': 'HTML',
            'render': ''
        },
        CONTENT_MARKDOWN: {
            'label': 'Markdown',
            'render': compile_markdown,
        },
        CONTENT_TEXTILE: {
            'label': 'Textile',
            'render': compile_textile,
        }
    }


PAGELET_CONTENT_DEFAULT
-------------------------

Default: `html`

This defines the default content type used when creating new pagelets. It can be either
a build-in content type or a user defined content type as described above.


PAGELET_USE_TAGGING
-----------------------

Default: `False`

There is optional support for including tags on pages with `django-tagging <http://code.google.com/p/django-tagging>`_.
You must have django-tagging installed.


PAGELET_USE_TAGGIT
-----------------------

Default: `False`

As an alternative to django-tagging there is support for including tags on pages with 
`django-taggit <https://github.com/alex/django-taggit>`_. You must have django-taggit installed.
It is not possible to use both `django-tagging` and `django-taggit` at the same time.


PAGELET_USE_TREENAV
-----------------------

Default: `False`

`django-treenav <https://github.com/caktus/django-treenav>`_ is another Django application maintained by Caktus. It is used to maintain
site navigation through the admin. You can tie you site navigation to pages created in Django
pagelets. You must have djange-treenav installed to use this setting.

