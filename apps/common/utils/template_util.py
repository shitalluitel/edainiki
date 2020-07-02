import re

from apps.common.constants import template_map as field_reference
from apps.setting.constants import NIBEDAN
from apps.setting.models import LetterTemplate


def clean_template(template):
    pattern = re.compile(r'\r\n\r\n|\r\n(\t)*')
    return pattern.sub('', template)


def generate_letter(instance, letter_template):
    letter_template = clean_template(letter_template)
    if instance:
        template_map = getattr(field_reference, instance.__class__.__name__.upper())
        for field_name in template_map.get('non_related_fields'):
            letter_template = replace_template(instance, field_name, letter_template)

        related_fields = template_map.get('related_fields')
        for key, value in related_fields.items():
            letter_template = parse_multiple_data(
                template=letter_template,
                fields=value,
                queryset=getattr(instance, key).all()
            )
        return letter_template
    return "Not able to generate template."


def replace_template(instance, field_name, letter_template):
    pattern = re.compile(r'{{ _ }}'.replace('_', field_name))
    letter_template = pattern.sub(str(getattr(instance, field_name)), letter_template)
    return letter_template


def get_multiple_pattern(template):
    pattern_str = r'<tr><td colspan="\d+">{{ multiple }}</td></tr>(.*)<tr><td colspan="\d+">{{ end_multiple }}</td>' \
                  r'</tr>|<p>{{ multiple }}</p>(.*)<p>{{ end_multiple }}</p>|{{ multiple }}(.*){{ end_multiple }}'
    return re.compile(pattern_str)


def parse_multiple_data(template, fields=None, queryset=None):
    pattern = get_multiple_pattern(template)
    result = add_multiple_data(
        template=pattern.search(template).group(1),
        fields=fields,
        queryset=queryset
    )
    return pattern.sub(result, template)


def add_multiple_data(template, fields, queryset):
    _data = []
    if queryset:
        for instance in queryset:
            _temp = template
            for field in fields:
                if hasattr(instance, field):
                    _temp = replace_template(
                        instance=instance,
                        field_name=field,
                        letter_template=_temp
                    )
            _data.append(_temp)
    return ''.join(_data)


def generate_form(form=None, formset=None):
    template_obj = LetterTemplate.objects.filter(
        model=form.instance.__class__.__name__,
        type=NIBEDAN
    ).first()
    if template_obj:
        template = clean_template(template_obj.template)
        fields = form.fields.keys()
        for field in fields:
            pattern = re.compile(r'{{ _ }}'.replace('_', field))
            _field_to_add = '{{ _ }}'.replace('_', f'form.{field}')
            template = pattern.sub(_field_to_add, template)
        if formset:
            template = generate_formset(template, formset)
        return '{% load widget_tweaks %}' + template
    return None


def generate_formset(template, formset):
    if callable(formset):
        formset = formset()

    fields = formset.form.base_fields.keys()
    pattern = get_multiple_pattern(template)
    try:
        _multiple = pattern.search(template).group(1)
    except AttributeError:
        return template

    get_table_data = re.compile(r'<tr>(.*)</tr>')
    _multiple_data = get_table_data.search(_multiple).group(1)
    start_formset = '''
        {% for formset_field in formset %}
            <tr class="item">
    '''
    remove_btn = '''
        <td style="border: 0.1px solid transparent;">
            <button type="button" class="btn btn-danger btn-sm remove-form-row" id="{{ formset.prefix }}">
                {% if formset_field.id %}
                   {{ formset_field.id | add_class:"formset-field" }}
                {% endif %}
                <i class="fa fa-minus"></i>
            </button>
        </td>
    '''
    end_formset = '''
        </tr>
        {% endfor %}
        <tr>
            <td style="border:0.1px solid transparent;">
                <button type="button" class="btn btn-sm btn-success add-form-row" id="{{ formset.prefix }}">
                    <i class="fa fa-plus"></i>
                </button>
            </td>
        </tr>
    '''
    for field in fields:
        field_pattern = re.compile(r'{{ _ }}'.replace('_', field))
        _field_to_add = '{{ _ }}'.replace('_', f'formset_field.{field}')
        _multiple_data = field_pattern.sub(_field_to_add, _multiple_data)

    formset_form = start_formset + _multiple_data + remove_btn + end_formset
    template = pattern.sub(formset_form, template)
    return template + '{{ formset.management_form }}'


def get_template_field_map(model_name, related=False):
    letter_template = LetterTemplate.objects.get(
        model=model_name,
        type=NIBEDAN
    )
    patt_match = re.compile(r'\{\{ ([\w_ ]+) \}\}').findall(clean_template(letter_template.template))
    field_map = getattr(field_reference, model_name.upper())
    return list(set(
        field_map.get(
            'non_related_fields' if not related else 'related_fields',
            []
        )
    ).intersection(set(patt_match)))
