from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,blank=True, null=True)
    parent = models.ForeignKey('self',blank=True, null=True,related_name='child', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"   

    def __str__(self):                           
        full_path = [self.name]            
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])