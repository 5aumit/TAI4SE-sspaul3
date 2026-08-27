from django.db import models
from employees.models import *


# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=30)
    department_dec = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.department_name


class Position(models.Model):
    position_name = models.CharField(max_length=30)

    def __str__(self):
        return self.position_name


class Contract(models.Model):
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    dep_id = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    pos_id = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    start_date = models.DateField('HireDate')
    end_date = models.DateField(
        default=None,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user_id.username

    def end_date_func(self):
        if self.end_date is None:
            return "Working"
        return self.end_date
