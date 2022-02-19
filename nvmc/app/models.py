from django.db import models

# Create your models here.
class Nvmc(models.Model):
    radios = models.CharField("選択", max_length=30)
    facility = models.CharField("設備", max_length=30)
    facNo = models.CharField("号機No", max_length=10)
    lot_id = models.CharField("ロットID", max_length=20)
    eqname = models.CharField("装置名", max_length=20)
    brname = models.CharField("品種名", max_length=20)
    description = models.TextField("故障現象", blank=True)

    def __str__(self) -> str:
        return self.radios