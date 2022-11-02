from django.db import models

class Item(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()

    def __str__(self):
        return self.name

class Purchase(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    date_purchase=models.DateField('date_published')

    def __str__(self):
        #return f"{}-{}"
        pass

