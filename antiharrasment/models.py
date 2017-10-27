from django.db import models

# Create your models here.
class query(models.Model):
    statement = models.TextField()
    is_harrassing = models.BooleanField()
    
    class Meta:
        verbose_name_plural = 'queries'

    def __str__(self):
        return self.statement
