from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nick_name = models.CharField(_('nick_name'),max_length=150,blank = True)
    avatar = models.ImageField(_('avatar'),blank=True)
    birthday = models.DateField(_('birthday'),null=True,blank=True)
    gender = models.models.NullBooleanField(_('gender'),help_text=_('female is false , male is true,null is unset'))
    province = models.ForeignKey(verbose_name=_(province),to ='Province',null=True,on_delete=models.SET_NULL)


    class Meta:
        db_table = 'user profiles'
        verbose_name = _('profile')    
        verbose_name_plural =_('profiles')
    @property
    def get_first_name(self):
        return self.user.first_name

    @property
    def get_last_name(self):
        return self.user.last_name
class User(AbstractBaseUser,PermissionsMixin):
    pass             