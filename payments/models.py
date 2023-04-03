from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.validators import validate_phone_number

class Gateway(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.ImageField(_('avatar'),blank=True,upload_to='categories/')
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='products/')
    is_enable=models.BooleanField(_('is enable'),default=True)
    #credentials= models.TextField(-('credentials'),blank = True)
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
        (STATUS_VOID,_('payment could  not be processed')),
        (STATUS_PAID,_('succesful')),
        (STATUS_ERROR,_('payment has encountered an error our technical team will check the bug ')),
        (STATUS_CANCELED,_('payment Canceled by user')),
        (STATUS_RFUNDED,_('this payment has been Refunded')),
    )
    user = models.ForeignKey('users.User',verbose_name=_('user'),related_name='%(class)s',on_delete=models.CASCADE)
    package = models.ForeignKey('subscriptions.Package',verbose_name=_('package'),related_name='%(class)s',on_delete=models.CASCADE)
    gateway = models.ForeignKey(Gateway,verbose_name=_('gateway'),related_name='%(class)s',on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField(_('price'),default=0)
    status = models.PositiveSmallIntegerField(_('status'),choices = STATUS_CHOICES,default=STATUS_VOID,db_index=True)
    device_uuid = models.CharField(_('device uuid'),max_length=40,blank=True)
    token = models.CharField(max_length=255)
    phone_number = models.BigIntegerField(_('phone number'),validators=[validate_phone_number],db_index=True)
    consumed_code = models.PositiveIntegerField(_('consumed reference code'),null=True,db_index=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True,db_index=True)
    updated_time = models.DateTimeField(_('modification time'),auto_now=True)
    
    class Meta:
        db_table = 'payments'
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')
    
    STATUS_TRANSLATION = {
        STATUS_VOID:_('payment')
    }