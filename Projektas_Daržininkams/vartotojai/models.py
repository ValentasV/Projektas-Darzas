import uuid as uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

class VartotojoAdministravimas(BaseUserManager):
    def create_user(self, vardas, pavarde, telefonas, elektroninis_pastas, password=None):
        if not elektroninis_pastas:
            raise ValueError('Vartotojas privalo įvesti savo el. pašto adresą')
        user = self.model(
            vardas=vardas,
            pavarde=pavarde,
            telefonas=telefonas,
            elektroninis_pastas=self.normalize_email(elektroninis_pastas),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, vardas, pavarde, telefonas, elektroninis_pastas, password=None):
        user = self.create_user(
            vardas=vardas,
            pavarde=pavarde,
            telefonas=telefonas,
            elektroninis_pastas=elektroninis_pastas,
            password=password,
        )
        user.admin = True
        user.superuser = True
        user.staff = True
        user.save(using=self._db)
        return user


class Vartotojas(AbstractUser):
    elektroninis_pastas = models.EmailField(
        verbose_name="El. pašto adresas",
        max_length=255,
        unique=True,
    )
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vardas = models.CharField(max_length= 50, verbose_name="Vardas", null=True, blank=True)
    pavarde = models.CharField(max_length= 50, verbose_name="Pavardė", null=True, blank=True)
    telefonas = models.CharField(max_length= 50, verbose_name="Telefono numeris", null=True, blank=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)


    objects = VartotojoAdministravimas()

    USERNAME_FIELD = "elektroninis_pastas"
    REQUIRED_FIELDS = ["vardas", "pavarde", "telefonas"]

    def __str__( self ):
        return f"{self.vardas} {self.pavarde}"

    class Meta:
        verbose_name = "Vartotojas"
        verbose_name_plural = "Vartotojai"


    def __str__(self):
        return self.email

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