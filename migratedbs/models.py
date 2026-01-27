from django.db import models, connections
from datetime import date

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    age = models.PositiveSmallIntegerField()
    registry_number = models.CharField(max_length=20, unique=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    company = models.CharField(max_length=100, blank=True, null=True)
    sector = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    address_number = models.CharField(max_length=20, blank=True, null=True)
    district = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    country = models.CharField(max_length=60, default='Brazil')
    post_code = models.CharField(max_length=12, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Person'
        managed = False
        ordering = ['id']

    def __str__(self):
        return f'{self.name} ({self.registry_number})'

    def computed_age(self):
        if not self.birth_date:
            return None
        today = date.today()
        years = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1
        return years

    @classmethod
    def using_mariadb(cls):
        """
        Helper to obtain a QuerySet that will read from the 'mariadb' DB connection.
        Uso: Person.using_mariadb().filter(...)
        """
        return cls.objects.using('mariadb')
