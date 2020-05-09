import re

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _

from apps.common.utils.commons import nep2eng


def area_validation(value):
    pattern = re.compile(r'((\d{1,2})*-*)*')
    if not pattern.match(value):
        raise ValidationError(
            _(
                'तपाईले पेस गर्नुभएको क्षेत्रफल मिलेन। कृपया बिग्घा-कट्ठा-धुर'
                ' मा राख्नुहोस्। प्रतेक इकाई  ० - २० सम्म मात्र लिईनेछ। '
            )
        )


def ward_validation(value):
    if isinstance(value, int):
        value = str(value)

    value = nep2eng(value)
    try:
        val = int(value)
    except ValueError:
        raise ValidationError(_('वार्ड नम्बर अंकमा हुनुपर्दछ ।'))

    if val > 39:
        raise ValidationError(_('वार्ड नम्बर ० - ३९ बीचमा हुनुपर्दछ ।'))
