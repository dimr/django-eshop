from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from binascii import hexlify
import os, uuid
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.conf import settings
import uuid


# from core.core import _createId

# Create your models here.


class ClientManager(BaseUserManager):
    def create_user(self, email, password, *args, **kwargs):
        try:
            print 'validating email'
            validate_email(email)
        except ValidationError, e:
            raise Exception("{email} is not a valid email address".format(email=email))

        if not email:
            raise ValueError("you must provide email")
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, *args, **kwargs)
        user.set_password(password)
	user.is_active=False
        user.save()
        return user

    def create_superuser(self, email, password, *args, **kwargs):
        superuser = self.create_user(email=email, password=password)
        superuser.is_staff = superuser.is_admin = superuser.is_superuser = True
        superuser.save()
        return superuser


def _createId():
    return hexlify(os.urandom(3))


class Client(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=60, unique=False, blank=True)
    last_name = models.CharField(max_length=65, unique=False, blank=True)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=70, blank=True)

    # password = models.CharField(max_length=10,blank=True,null=False)
    # password = models.CharField(blank=True, null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', ]

    objects = ClientManager()

    def get_short_name(self):
        return self.username

    @property
    def get_full_name(self):
        full_name = '{first} {second}'.format(first=self.first_name, second=self.last_name)
        return full_name


def gen_uuid():
    return str(uuid.uuid4()).replace('-', '')


class ClientProfile(models.Model):
    the_client = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, related_name='profile',
                                      primary_key=True)
    profile_url = models.CharField(default=gen_uuid, max_length=255)
    address = models.CharField(max_length=30, unique=False, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return str(self.pk)


from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = ClientProfile(the_client=instance)
        profile.save()
