from django.db import models
import random
from django.utils.translation import gettext_lazy as _
from wsgiref.validate import validator
from django.core.validators import RegexValidator
from django.core.validators import BaseValidator
from django.core.mail import send_mail
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionsMixin,UserManager
from django.utils import timezone
class UserManager(BaseUserManager):
    use_in_migrations = True  
    def _create_user(self,username,phone_number,email,password,is_staff,is_superuser,**extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number,username=username,email=email,
                          is_staff=is_staff,is_active=True,is_superuser=is_superuser,date_joined=now,**extra_fields)    
        if not extra_fields.get('no password'):
            user.set_password(password)
        user.save(using=self._db)
        return user    
    def create_user(self,username=None,phone_number=None,email=None,password=None,**extra_fields):
        if username is None:#bebinim username dade ya  na 
            if email:
                username = email.split('@',1)[0] #agar username nadad bayad khodemoon barash besazim 
        
            if phone_number:
                username = random.choice ('abcdefghijklmnopqrstuvwxyz')+str(phone_number)[-7:]
            while User.objects.filter(username=username).exists():
                username += str(random.randint(10,99))
        return self._create_user(username,phone_number,email,password,False,False,**extra_fields)
    
    def create_superuser(self,username,phone_number,email,password,**extra_fields):            
        return self._create_user(username,phone_number,email,password,True,True,**extra_fields)
        

class User(AbstractBaseUser,PermissionsMixin):
    #avstract basre class implement a fully featured user model with admin compliant permissions
    username = models.CharField(_('username'),max_length=32,unique=True,help_text=_('Required. 30 characters or fewer starting with a letter. Letters,digits'),
    validators=[RegexValidator(r'^[a-zA-Z][a-zA-Z0-9_\.]+$',
                                         _('Enter a valid username starting with a-z this value mauy contain ony letters numbers and underscore character '),
                                         'invalid')],error_messages={'unique':_("A user with that username already exists."),})
    first_name = models.CharField(_('first name'),max_length=30,blank=True)
    last_name = models.CharField(_("last name"), max_length=30,blank=True)
    email = models.EmailField(_("email address"),unique=True,null=True,blank=True )
    phone_number = models.BigIntegerField(_("mobile number"),unique = True,null = True, blank=True,
                                          validators=[RegexValidator(r'^989[0-3,9]\d(8)$',('Enter a valid mobile number')),],
                                          error_messages={'unique':_("A user with this mobile number already exists.")})
    is_staff = models.BooleanField(_("staff status"),default=False,help_text=_('Designates wheather the user can log into this admin site,'))
    is_active = models.BooleanField(_("active"),default=True,help_text=_('Designated whether this user should be treared as active,unset this instead of deleting accounts'))
    date_joined = models.DateTimeField(_("date joind"), default=timezone.now)
    last_seen = models.DateTimeField(_("last seen date"),null=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['email','phone_number']
    class Meta:
        db_table = 'users'
        verbose_name =_('user')
        verbose_name_plural = _('users')
    def get_full_name(self):
        full_name = '%s %s' %(self.first_name,self.last_name)        
    def get_short_name(self):
        return self.first_name
    def email_user(self,subject,message,from_email=None,**kwargd):
        send_mail()
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nick_name = models.CharField(_('nick_name'),max_length=150,blank = True)
    avatar = models.ImageField(_('avatar'),blank=True)
    birthday = models.DateField(_('birthday'),null=True,blank=True)
    gender = models.BooleanField(_('gender'),help_text=_('female is false , male is true,null is unset'))
    province = models.ForeignKey(verbose_name=_('province'),to ='Province',null=True,on_delete=models.SET_NULL)
    #email = models.EmailField(_("email address"),blank=True)
    #phone_numner = models.BigIntegerField(_("mobile number"),unique = True,null=True,null = True, blank=True,
    # validators=[validator.RegexValidator(r'^989[0-3,9]\d(8)$',('Enter a valid mobile number')),],
    # error_messages={'unique':_("A user with this mobile number already exists.")})


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
    def get_nickname(self):
        return self.nick_name if self.nick_name else self.user.username
class Device(models.Model):
    WEB = 1
    IOS = 2
    ANDROID = 3
    DEVICE_TYPE_CHOICES = (
        (WEB,'web'),
        (IOS,'ios'),
        (ANDROID,'android')
    )
    user = models.ForeignKey(User,related_name ='devices', on_delete=models.CASCADE)
    device_uuid = models.UUIDField(_("Device UUID"),null=True)
    notify_token = models.CharField(_("Notification Token"), max_length=200,blank=True,
                                    validators=[RegexValidator(r'^([a-z]|[A-z]|[0-9])\w+',_('Notify token is not valid '),'invalid')])
    last_login = models.DateTimeField(_('last ;ogin date'),null=True)
    device_type = models.PositiveIntegerField(choices=DEVICE_TYPE_CHOICES,default=ANDROID)
    device_os = models.CharField(_("device os "), max_length=20,blank=True)
    device_model = models.CharField(_("device model"), max_length=50,blank=True)
    app_version = models.CharField(_("app version"), max_length=20,blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'user_devices'
        verbose_name = _('device')
        verbose_name_plural = _('devices')
        unique_together = ('user','device_uuid')
class Province(models.Model):
    name = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.name
