from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(_("اسم النوع"), max_length=50)
    icon = models.ImageField(_("الصورة"), upload_to="category_icons",null=True,blank=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

class Box(models.Model):
    name = models.CharField(_("اسم الصندوق"), max_length=50)
    image = models.ImageField(_("الصورة"), upload_to="boxes")
    price = models.FloatField(_("السعر"))
    category = models.ForeignKey(Category, verbose_name=_("النوع"), on_delete=models.CASCADE,null=True)
    products = models.ManyToManyField("Product", verbose_name=_("المنتجات"))
    slug = models.SlugField(_("slug"),blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Box, self).save(*args,**kwargs)


    class Meta:
        verbose_name = _("Box")
        verbose_name_plural = _("Boxes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("root:Box_detail", kwargs={"slug": self.slug})

class SpinNumber(models.Model):
    spin_number = models.IntegerField(_("رقم الللفة"))

    def __str__(self):
        return str(self.spin_number)

    class Meta:
        ordering = ["spin_number"]

class Product(models.Model):
    name = models.CharField(_("اسم المنتج"), max_length=50)
    image = models.ImageField(_("الصورة"), upload_to="products")
    price = models.FloatField(_("السعر"))
    description = models.TextField(_("الوصف"))
    spin_number = models.ManyToManyField(SpinNumber, verbose_name=_("رقم اللفات"))
    message = models.ForeignKey("root.Message", verbose_name=_("الرسالة"), on_delete=models.CASCADE,blank=True,null=True)
    slug = models.SlugField(_("slug"),blank=True,null=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("root:Product_detail", kwargs={"slug": self.slug})

class Message(models.Model):
    title = models.CharField(_("عنوان الرسالة"), max_length=50,null=True,blank=True)
    content = RichTextField(_("محتوي الرسالة"),null=True,blank=True)

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

    def __str__(self):
        return self.title

class BoxSpin(models.Model):
    player = models.ForeignKey("root.Player", verbose_name=_("اللاعب"), on_delete=models.CASCADE)
    box = models.ForeignKey(Box, verbose_name=_("الصندوق"), on_delete=models.CASCADE)
    spin = models.IntegerField(_("عدد اللفات"))

    class Meta:
        verbose_name = _("BoxSpin")
        verbose_name_plural = _("BoxSpins")

    def __str__(self):
        return f'{str(self.box)} > {str(self.spin)}'

class Prize(models.Model):
    player = models.ForeignKey("root.Player", verbose_name=_("اللاعب"), on_delete=models.CASCADE)
    prize = models.ForeignKey(Product, verbose_name=_("الجائزة"), on_delete=models.CASCADE)
    box = models.ForeignKey(Box, verbose_name=_("الصندوق"), on_delete=models.CASCADE)
    winning_numbers = models.IntegerField(_("عدد مرات الفوز"))

    class Meta:
        verbose_name = _("Prize")
        verbose_name_plural = _("Prizes")

    def __str__(self):
        return f'{str(self.box)} =>{str(self.prize)}: {str(self.winning_numbers)}'

class Player(models.Model):
    player = models.OneToOneField(User, verbose_name=_("اللاعب"), on_delete=models.CASCADE)
    balance = models.FloatField(_("الرصيد"),null=True,blank=True)
    boxes_spin = models.ManyToManyField(Box, verbose_name=_("لفات الصناديق"),through=BoxSpin,blank=True)
    prizes = models.ManyToManyField(Product, verbose_name=_("الجوائز"),through=Prize,blank=True)

    class Meta:
        verbose_name = _("Player")
        verbose_name_plural = _("Players")

    def __str__(self):
        return str(self.player)

class Classification(models.Model):
    facebook = models.URLField(_("لينك حساب الفيس"), max_length=200,null=True,blank=True)
    twitter = models.URLField(_("لينك حساب التويتر"), max_length=200,null=True,blank=True)
    google = models.URLField(_("لينك حساب جوجل"), max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = _("Classification")
        verbose_name_plural = _("Classifications")

    def __str__(self):
        return self.facebook

def create_player(sender, **kwargs):
    if kwargs["created"]:
        Player.objects.create(player=kwargs["instance"],balance=0)

post_save.connect(create_player , sender=User)
