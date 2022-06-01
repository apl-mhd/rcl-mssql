from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _  
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


class UserAccount(models.Model):
    
    USER_ID = models.BigIntegerField(primary_key=True)
    USER_NAME = models.CharField(max_length=50)
    LOGIN_NAME = models.CharField(max_length=50)
    PASSWORD = models.TextField()
    SWAP_CARD = models.CharField(max_length=50)
    ACCESS_LEVEL = models.CharField(max_length=50)
    REG_DATE = models.DateTimeField(auto_now_add=True)
    STATUS = models.CharField(max_length=50)
    CREATED_BY = models.BigIntegerField()

    class Meta:
        db_table = 'USER_ACCOUNT'






class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    login_name = models.CharField(_('login name'), max_length=30, unique=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    admin = models.BooleanField(_('admin'), default=True)
    status = models.BooleanField(_('status'), default=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'login_name'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

  


