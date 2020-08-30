from office.models import OfficeModel
from django.db import models

agg = OfficeModel.objects.aggregate(models.Avg('price'), models.Max('price'))
agg = OfficeModel.objects.order_by('name')[2:2]
