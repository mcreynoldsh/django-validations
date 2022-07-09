from django.db import models
from django.core.exceptions import ValidationError # import ValidationError from Django
from django.utils.translation import gettext_lazy as text
from django.core.validators import * 
from django.utils import timezone
from datetime  import datetime

def validate_stroke_type(stroke_type):
    valid_stroke_types = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if stroke_type not in valid_stroke_types:
        raise ValidationError(text(f"{stroke_type} is not valid stroke"))

class SwimRecord(models.Model):
    first_name = models.CharField(max_length=61)
    last_name = models.CharField(max_length=61)
    team_name = models.CharField(max_length=61)
    relay = models.BooleanField()
    stroke = models.CharField(max_length=61, validators=[validate_stroke_type])
    distance = models.IntegerField(validators=[MinValueValidator(50)])
    record_date = models.DateTimeField(validators=[MaxValueValidator(timezone.now())])
    record_broken_date = models.DateTimeField(validators=[MinValueValidator(record_date)])
