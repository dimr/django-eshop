from django.db import models
from django.conf import settings
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.conf import settings
import uuid,json

#http://stackoverflow.com/questions/2680391/in-django-changing-the-file-name-of-uploading-file
def product_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.product.slug, filename)


class Product(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    sales_price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(unique=True)

    time_stamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    # image = models.ImageField(upload_to=product_directory_path, blank=True)


    def first_pic(self):
        at_least_one_main = [pic.main==True for pic in self.product_images.all()].count(True)

        try:
            if at_least_one_main >= 1:
                return [pic.image.url for pic in self.product_images.all() if pic.main is True][0]
            else:
                temp = self.product_images.all()[0]
                temp.main=True
                temp.save()
                print(self.title,self.product_images.all()[0])
                return temp.image.url
        except IndexError:
            pass



    class Meta:
        unique_together = ('title', 'slug')

    def admin_image(self):
        if Product.objects.get(pk=self.pk).products.all().count() != 0:
            try:
                return mark_safe(u'<img src="%s" width=60 height=60/>' % self.products.all()[0].image.url)
            except Exception:
                pass

    admin_image.allow_tags = True

    def get_absolute_url(self):
        return reverse('single_product',kwargs={'slug':self.slug})


    def all_pics(self):
        return json.dumps({pic.name:pic.image.url for pic in self.product_images.all()})

    def __unicode__(self):
        return self.title


def gen_uuid():
        return str(uuid.uuid4()).split('-')[0]


class ProductImage(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False,default=gen_uuid,editable=True)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to=product_directory_path, blank=True)
    main = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.DateTimeField(auto_now_add=False, auto_now=True)


    class Meta:
        # order_with_respect_to = 'product'
        ordering = ['updated']

    def thumb(self):

        return self.image.url

    def large_pic(self):
        if self.image:
            return mark_safe(u'<img src="%s" />' % self.image.url)
        return 'no image available'

    large_pic.short_description = 'Picture'




    def __unicode__(self):
        # return mark_safe(u'<img src="%s" width=100 height=100/>' % self.image.url)
        return self.product.title


@receiver(post_delete, sender=ProductImage)
def post_delete_handler(sender, **kwargs):
    pic = kwargs['instance']
    storage, path = pic.image.storage, pic.image.path
    print storage, path
    print os.path.dirname(path)
    folder_location = os.path.dirname(os.path.realpath(path))
    storage.delete(path)
    # if not os.listdir(folder_location)
    if os.listdir(folder_location) == []:
        os.rmdir(folder_location)
        # storage.delete(os.path.dirname(folder_location))
