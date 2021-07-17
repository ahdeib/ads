from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from categories.models import Categories
#from .models import Categories
# from django.core.urlresolvers import reverse
# Create your models here.


class Product(models.Model):
    PRDName = models.CharField(max_length=100 , verbose_name=_("Product Name "))
    #PRDCategory = models.ForeignKey(Categories , on_delete=models.CASCADE , blank=True, null=True ,verbose_name=_("Category "))
    PRDCategory = models.ForeignKey(Categories, on_delete=models.CASCADE , blank=True, null=True ,verbose_name=_("Category "))


    #PRDBrand = models.ForeignKey('settings.Brand' , on_delete=models.CASCADE , blank=True, null=True ,verbose_name=_("Brand "))
    PRDDesc = models.TextField(verbose_name=_("Description"))
    PRDImage = models.ImageField(upload_to='prodcut/' , verbose_name=_("Image") , blank=True, null=True)
    PRDPrice = models.DecimalField(max_digits=5  , decimal_places=2 , verbose_name=_("Price"))
    PRDDiscountPrice = models.DecimalField(max_digits=5  , decimal_places=2 , verbose_name=_("Discount Price"))    
    PRDCost = models.DecimalField(max_digits=5 , decimal_places=2 , verbose_name=_("Cost"))
    PRDCreated = models.DateTimeField(verbose_name=_("Created At"))

    PRDSLug = models.SlugField(blank=True, null=True , verbose_name=_("Product URL"))
    PRDISNew = models.BooleanField(default=True , verbose_name=_("New Product "))
    PRDISBestSeller = models.BooleanField(default=False , verbose_name=_("Best Seller"))


    def save(self , *args , **kwargs):
        if not self.PRDSLug :
            self.PRDSLug = slugify(self.PRDName)
        super(Product , self).save(*args , **kwargs)
    
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.PRDSLug})

    def __str__(self):
        return self.PRDName


class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(Product , on_delete=models.CASCADE , verbose_name=_("Product"))
    PRDIImage = models.ImageField(upload_to='prodcut/' , verbose_name=_("Image"))

    def __str__(self):
        return str(self.PRDIProduct)
