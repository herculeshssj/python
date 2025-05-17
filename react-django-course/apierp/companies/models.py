from django.db import models

# Create your models here.
class Enterprise(models.Model):
    name = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name