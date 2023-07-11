from django.db import models

class category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    Descrição = models.TextField(blank=True, null=True)
    Preço = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    foi_vendido = models.BooleanField(default=False)

    def __str__(self):
        return self.name