import re

from django.conf import settings
from django.template.defaultfilters import slugify


def unique_slugify(instance, value, slug_field_name='slug', queryset=None, slug_separator='-'):
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_length = slug_field.max_length

    slug = slugify(value)
    if slug_length:
        slug = slug[:slug_length]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create a queryset, excluding the current instance.
    if not queryset:
        queryset = instance.__class__._default_manager.all()
        if instance.pk:
            queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '-%s' % next
        if slug_length and len(slug) + len(end) > slug_length:
            slug = slug[:slug_length - len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator=None):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
        value = re.sub('%s+' % re_sep, separator, value)
    return re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)


def extract_related_model_fields(obj):
    related_objects = obj._meta.related_objects
    related_object_fields = {}
    for related_object in related_objects:
        related_model = related_object.related_model
        fields, meta_data = extract_fields(related_model, is_related=True)
        related_object_fields[meta_data.verbose_name] = fields
    return related_object_fields


def extract_fields(related_model, is_related=False):
    meta_data = related_model._meta
    # if is_related:
    #     get_field = filter(
    #         lambda x: not (isinstance(x, models.ForeignKey)),
    #         meta_data.get_fields()
    #     )
    # else:
    get_field = meta_data.get_fields()
    fields = list(
        filter(
            lambda x: x not in settings.EXCLUDE_FIELDS,
            map(
                lambda x: x.name,
                get_field
            )
        )
    )
    return fields, meta_data
