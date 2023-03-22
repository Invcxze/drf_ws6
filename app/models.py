from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=50)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class Order(models.Model):
    table_number = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status_choices = (
        ('added', 'Добавлен'),
        ('preparing', 'Готовится'),
        ('ready', 'Готов'),
        ('canceled', 'Отменен'),
        ('paid', 'Оплачен'),
    )
    status = models.CharField(max_length=20, choices=status_choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
