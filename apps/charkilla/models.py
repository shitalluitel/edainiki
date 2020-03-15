from django.db import models

# Create your models here.
from apps.common.models.common import BaseModel
from apps.common.validators.commons import area_validation


class Charkilla(BaseModel):
    pass


class CharkillaDetail(models.Model):
    charkilla = models.ForeignKey(Charkilla, related_name="charkilla_details", on_delete=models.DO_NOTHING)
    kitta_no = models.CharField(
        max_length=16,
        error_messages={'max_length': 'कृपया कित्ता नंको लम्बाई १६ भन्दा कम राख्नुहोस।'}
    )
    map_sheet_no = models.CharField(
        max_length=16,
        error_messages={'max_length': 'कृपया कित्ता नंको लम्बाई १६ भन्दा कम राख्नुहोस।'}
    )
    total_area = models.CharField(max_length=8, validators=[area_validation])
    east_piller = models.CharField(
        max_length=132,
        error_messages={'max_length': 'कृपया लम्बाई 132 भन्दा कम राख्नुहोस।'},
    )
    west_piller = models.CharField(
        max_length=132,
        error_messages={'max_length': 'कृपया लम्बाई 132 भन्दा कम राख्नुहोस।'},
    )
    north_piller = models.CharField(
        max_length=132,
        error_messages={'max_length': 'कृपया लम्बाई 132 भन्दा कम राख्नुहोस।'},
    )
    south_piller = models.CharField(
        max_length=132,
        error_messages={'max_length': 'कृपया लम्बाई 132 भन्दा कम राख्नुहोस।'},
    )
    description = models.CharField(max_length=264, null=True, blank=True,
                                   error_messages={'max_length': 'कृपया कैफियतको लम्बाई २५० भन्दा कम राख्नुहोस |'})
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.four_piller.applicant_name + ", kitta number:  " + self.kitta_no)
