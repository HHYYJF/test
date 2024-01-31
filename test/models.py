from django.db import models

class Requisite(models.Model):
    payment = (
        ('Карта','Карта'),
        ('Cчет','Платежный счет'),
    )
    pay = models.CharField(max_length=10, choices=payment,verbose_name='Способы оплаты')
    account = models.CharField(max_length=50,verbose_name="Счет")
    owner = models.CharField(max_length=100,verbose_name="ФИО ладелеца")
    number = models.CharField(max_length=12,verbose_name="Номер телефона")
    limit = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="лимит")

    class Meta:
        verbose_name_plural = 'Реквизиты'

    def __str__(self):
        return f"{self.owner} - {self.number}"


class PaymentRequest(models.Model):
    status_kart = (
        ('Ожидает', 'Ожидает оплаты'),
        ('Оплачена', 'Оплачена'),
        ('Отменена', 'Отменена'),
    )
    id = models.AutoField(primary_key=True,verbose_name='ID заявки')
    sum = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Сумма")
    req = models.ForeignKey(Requisite, on_delete=models.CASCADE,verbose_name="Реквизиты")
    status = models.CharField(max_length=10, choices=status_kart,verbose_name="Статус")

    class Meta:
        verbose_name_plural = 'Платежный запрос'

    def __str__(self):
        return f"Заявка {self.req.owner} {self.status}"
