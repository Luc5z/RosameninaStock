from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=300, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to="produtos/", default="" )
    onstore = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Sale(models.Model):
    sale_id = models.AutoField
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2) 
    date = models.DateField(auto_now_add=True)
    client = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="", blank=True, null=True)
    PAYMENT_CHOICES = [
        ('dinheiro', 'Dinheiro'),
        ('pix', 'Pix'),
        ('debito', 'Débito'),
        ('credito', 'Crédito'),
    ]
    payment = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default="dinheiro")

    def __str__(self):
        return f"{self.product.name} - {self.client} ({self.date})"
    
    class Meta:
        ordering = ['-id']