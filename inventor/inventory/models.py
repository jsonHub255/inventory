from django.db import models

# Create your models here.
class Engin(models.Model):
    eng_name = models.CharField(max_length=64)
    eng_code = models.CharField(max_length=64)
    ch_name = models.CharField(max_length=64)
    # eng_date = models.DateTimeField()
    
    # Formatted String formt to show data.
    def __str__(self):
        return f"{self.id} For: name: {self.eng_name} Code: {self.eng_code} Chantier: {self.ch_name} DATE: "
    
