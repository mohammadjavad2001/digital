from django.db import models
from utils.validators import validate_sku
from django.core.validators import BaseValidator
from django.utils.translation import gettext_lazy as _
class Package(models.Model):
    title = models.CharField(_("title"), max_length=150)
    sku = models.CharField(_("stock keeping unit"), max_length=20,validators=[validate_sku],db_index=True)
    description = models.TextField(_("desciption"),blank=True)
    avatar = models.ImageField(_("avatar"), upload_to='packages/',blank=True)
    is_enable = models.BooleanField(_("is enable"),default=True)
    price = models.PositiveIntegerField(_("price"))
#    gateways = models.ManyToManyField("payments,Gateway")
    duration = models.DurationField(_("duration"),blank=True,null=True)
    created_time = models.DateTimeField(_("created time"),auto_now_add=True)
    updated_time = models.DateTimeField(_("updated time"), auto_now_add=True)

    class Meta:
        db_table = 'packages'
        verbose_name =_('Package')
        verbose_name_plural = _('Packages ')
    def __str__(self):
        return self.title

class Subscription(models.Model):
    user = models.ForeignKey("users.User",related_name='%(class)s', on_delete=models.CASCADE)
    package = models.ForeignKey(Package, related_name='%(class)s', on_delete=models.CASCADE)
    created_time = models.DateTimeField(_("created time "), auto_now_add=True)
    expire_time =models.DateTimeField(_('expire time'),blank=True,null=True)

    class Meta:
        db_table = 'subscription'
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions ')                    
    