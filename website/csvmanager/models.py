from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, name, university_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not name:
            raise ValueError("Users must enter a name")
        if not university_name:
            raise ValueError("User must enter University name")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            university_name=university_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, university_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,
            university_name=university_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(verbose_name="email", max_length=200, unique=True)
    name = models.CharField(verbose_name="name", max_length=200, null=True)
    university_name = models.CharField(verbose_name="university name", max_length=200, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'university_name']

    objects = MyAccountManager()

    def __str__(self):
        return '%s | %s' % (self.name, self.email)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class CSVFile(models.Model):
    STATUS = (
        ('Idle', 'Idle'),
        ('Processing', 'Processing'),
        ('Done', 'Done'),
    )
    NETWORK = (
        ('Public', 'Public'),
        ('Private', 'Private')
    )
    uploader = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=200, null=True)
    csv = models.FileField(upload_to='%Y/%m/%d/', null=True)
    network = models.CharField(max_length=60, null=True, choices=NETWORK)
    status = models.CharField(default='Idle', max_length=60, null=True, choices=STATUS, editable=False)
    result_csv = models.FileField(default='', null=True, editable=False)

    def __str__(self):
        return self.title
