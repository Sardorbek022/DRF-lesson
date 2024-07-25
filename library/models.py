from django.db import models


class BookModel(models.Model):
    
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.author} : {self.title}"
    
    class Meta:
        db_table = 'Books'
        managed = True
        verbose_name = 'Book'
        verbose_name_plural = 'Books'