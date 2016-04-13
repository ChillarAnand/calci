from simpleeval import simple_eval
from django.db import models
from swampdragon.models import SelfPublishModel
from .serializers import CalculationSerializer


class Calculation(SelfPublishModel, models.Model):

    serializer_class = CalculationSerializer

    expression = models.CharField(max_length=255)
    result = models.CharField(max_length=40, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.result = simple_eval(self.expression)
        super(Calculation, self).save(*args, **kwargs)

    def __str__(self):
        return '{} = {}'.format(self.expression, self.result)
