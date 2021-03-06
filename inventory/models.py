from django.db import models

from django.db.models import ForeignKey
from django.db.models import CharField, PositiveIntegerField, DateField, IntegerField, TextField, DecimalField, \
    ManyToManyField

from core.models import SoftDeletionModel
# Create your models here.

MOVEMENT_TYPE = [
    ('G', 'Get'),
    ('R', 'Return')
]


class Shuttle(SoftDeletionModel):
    plate_number = CharField(max_length=6, unique=True)
    make = CharField(max_length=64)
    model = CharField(max_length=64)
    date_acquired = DateField()

    def __str__(self):
        return f"{self.id} - {self.make} - {self.model}"


class Item(SoftDeletionModel):
    name = CharField(max_length=64)
    quantity = PositiveIntegerField()
    brand = CharField(max_length=64)
    vendor = CharField(max_length=64)
    unit_price = PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"


class UsedItem(SoftDeletionModel):
    item = ForeignKey(Item, on_delete=models.CASCADE)
    quantity = IntegerField()


class RepairProblem(SoftDeletionModel):
    description = TextField(max_length=255)


class RepairFinding(SoftDeletionModel):
    description = TextField()


class RepairModifications(SoftDeletionModel):
    item_used = ForeignKey(Item, on_delete=models.CASCADE)
    quantity = PositiveIntegerField()
    description = TextField()


class Repair(SoftDeletionModel):
    shuttle = ForeignKey(Shuttle, on_delete=models.PROTECT)
    date = DateField()
    labor_fee = DecimalField(max_digits=10, decimal_places=2)
    problems = ManyToManyField(RepairProblem)
    findings = ManyToManyField(RepairFinding)
    modifications = ManyToManyField(RepairModifications)


# TODO @Paolo I don't know the fields for this
class ItemMovement(SoftDeletionModel):
    item = ForeignKey(Item, on_delete=models.PROTECT)
    type = CharField(max_length=1, choices=MOVEMENT_TYPE)
    quantity = PositiveIntegerField()
    repair = ForeignKey(Repair, on_delete=models.PROTECT)

# TODO - fill these up

# class PreventiveMaintenance(SoftDeletionModel):
# class ItemMovement(SoftDeletionModel):
