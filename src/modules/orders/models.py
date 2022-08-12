from django.db import models
import uuid

class Order(models.Model):
    """
    Заказ
    
    Каждый экземпляр может существовать только в полностью заполненном виде.

    Помимо основных полей, хранит в себе дату создания, дату изменения и uuid. На случай, если пользователь начнёт создавать дубли.
    """
    number = models.IntegerField()
    order = models.CharField(max_length=7)
    price_in_dollars = models.IntegerField()
    price_in_rubles = models.IntegerField()
    delivery_date = models.DateField()

    created_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    deleted_from_file = models.BooleanField(default=True)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['number']
