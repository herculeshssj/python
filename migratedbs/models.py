from django.db import models, connections
from datetime import date

class PersonMySQL(models.Model):
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

import uuid
from datetime import date
from django.db import models

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    age_persisted = models.PositiveSmallIntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "person"
        indexes = [
            models.Index(fields=["name"], name="idx_person_name"),
        ]

    def __str__(self):
        return self.name

    @property
    def age(self) -> int | None:
        if not self.birth_date:
            return None
        today = date.today()
        years = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1
        return years


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.OneToOneField(
        Person,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="employee",
    )
    registry_number = models.CharField(max_length=100, unique=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    company = models.CharField(max_length=255, null=True, blank=True)
    sector = models.CharField(max_length=255, null=True, blank=True)
    hired_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "employee"
        indexes = [
            models.Index(fields=["registry_number"], name="idx_employee_registry"),
        ]

    def __str__(self):
        return f"{self.registry_number} - {self.person.name if self.person else 'N/A'}"


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="addresses",
    )
    address_name = models.CharField(max_length=255)
    address_number = models.CharField(max_length=50)
    district = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, default="Brazil")
    post_code = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "address"
        indexes = [
            models.Index(fields=["person"], name="idx_address_person"),
        ]

    def __str__(self):
        return f"{self.address_name}, {self.address_number} - {self.city or ''}"
