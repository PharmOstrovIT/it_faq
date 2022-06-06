from django.db import models


class Equipment(models.Model):

    apteka_id = models.DecimalField(max_digits=10, decimal_places=0)
    equipment_type = models.CharField(max_length=200)
    equipment_model = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200, unique=True)
    purchase_date = models.DateField()
    invoice_number = models.CharField(max_length=200)
    invoice_date = models.DateField()
    purchase_org = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)

    def __str__(self):
        return self.apteka_id

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
