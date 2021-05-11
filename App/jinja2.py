from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment
import widget_tweaks
# from offers.templatetags import form_tags
from django.contrib.humanize.templatetags.humanize import naturaltime
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field
import mail_templated

def environment(**options):
    env = Environment(**options)
    env.globals.update({'static': staticfiles_storage.url,
                        'url': reverse,
                        'widget_tweaks': widget_tweaks,
                        # 'form_tags': form_tags,
                        'naturaltime': naturaltime,
                        'as_crispy_field': as_crispy_field,
                        'mail_templated': mail_templated,
                        })

    return env
