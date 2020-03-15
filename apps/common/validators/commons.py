import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def area_validation(value):
    pattern = re.compile(r'((\d{1,2})*-*)*')
    if not pattern.match(value):
        raise ValidationError(
            _(
                'तपाईले पेस गर्नुभएको क्षेत्रफल मिलेन। कृपया बिग्घा-कट्ठा-धुर'
                ' मा राख्नुहोस्। प्रतेक इकाई  ० - २० सम्म मात्र लिईनेछ। '
            )
        )
