from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.validators import validate_phone_number

class Gateway(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.ImageField(_('avatar'),blank=True,upload_to='categories/')
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='products/')
    is_enable=models.BooleanField(_('is enable'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    update_time = models.DateTimeField(_('updated time'),auto_now=True)
    class Meta:
        db_table= 'gateways'
        verbose_name =_('Gateway')
        verbose_name_plural=_('Gateway')
class Payment(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_ERROR = 20
    STATUS_CANCELED = 30
    STATUS_RFUNDED = 31
    STATUS_CHOICES = (
        (STATUS_VOID,-('Void')),
        (STATUS_PAID,-('Paid')),
        (STATUS_ERROR,-('Error')),
        (STATUS_CANCELED,-('User Canceled')),
        (STATUS_RFUNDED,-('Refunded')),
    )

    STATUS_TRANSLATION = {
        STATUS_VOID:_('payment ')
    }