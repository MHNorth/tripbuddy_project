from django.utils.text import slugify
import re

def unique_slug_generator(mode_instance, title, slug_field):

    slug = slugify(title)
    model_class = model_instance._class_

    while model_class._default_manager.filter(slug=slug).exists():
        object_pk = model_class._default_manager.latest('pk')
        object_pk = object_pk.pk + 1

        slug = f'{slug}-{object_pk}'

    return slug