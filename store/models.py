from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
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
    price = models.IntegerField(default=0, editable=False) 
    date = models.DateField(auto_now_add=True)
    client = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.product.price
        super(Sale, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.product