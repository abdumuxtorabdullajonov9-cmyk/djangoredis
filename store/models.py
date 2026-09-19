from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    stock = models.IntegerField(verbose_name="Qoldiq")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
