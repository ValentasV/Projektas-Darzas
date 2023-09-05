import uuid as uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

class VartotojoAdministravimas(BaseUserManager):
    def create_user(self, first_name, last_name, phone, email, password=None):
        if not email:
            raise ValueError('Vartotojas privalo įvesti savo el. pašto adresą')
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, phone, email, password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password,
        )
        user.admin = True
        user.superuser = True
        user.staff = True
        user.save(using=self._db)
        return user


class Vartotojas(AbstractUser):
    email = models.EmailField(
        verbose_name="El. pašto adresas",
        max_length=255,
        unique=True,
    )
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length= 50, null=True, blank=True)
    phone = models.CharField(max_length= 50, verbose_name="Telefono numeris", null=True, blank=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)


    objects = VartotojoAdministravimas()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone"]

    def __str__( self ):
        return f"{self.first_name}"

    class Meta:
        verbose_name = "Vartotojas"
        verbose_name_plural = "Vartotojai"


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin