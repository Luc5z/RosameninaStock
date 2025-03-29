from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=50, default="")
    categoria = models.CharField(max_length=50, default="")
    cor = models.CharField(max_length=50, default="")
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=300, blank=True, null=True)
    quantidade = models.IntegerField(default=1)
    imagem = models.ImageField(upload_to="produtos/", default="" )
    naloja = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome
    
class Sale(models.Model):
    sale_id = models.AutoField
    produto = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    nome_venda = models.CharField(max_length=50, default="")
    quantidade = models.IntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2) 
    data = models.DateField(auto_now_add=True)
    cliente = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="", blank=True, null=True)
    PAYMENT_CHOICES = [
        ('Dinheiro', 'Dinheiro'),
        ('Pix', 'Pix'),
        ('Debito', 'Débito'),
        ('Credito', 'Crédito'),
    ]
    pagamento = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default="dinheiro")

    def save(self, *args, **kwargs):
        if self.produto and not self.nome_venda:
            self.nome_venda = self.produto.nome
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_venda} - {self.cliente} ({self.data})"
    
    class Meta:
        ordering = ['-id']
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"