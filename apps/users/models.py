from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password, check_password
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    def _create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError("The given phone must be set")

        user = self.model(phone=phone, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone, password, **extra_fields)


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = ("male", "Мужской")
        FEMALE = ("female", "Женский")

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS: list[str] = []

    username = None
    phone = models.CharField(max_length=50, unique=True)
    birthdate = models.DateField(null=True, blank=True)
    zip_code = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    address1 = models.CharField(max_length=100, null=True, blank=True)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=Gender.choices, null=True, blank=True)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.full_name} ({self.phone})"

    def change_password(self, current_password: str, new_password1: str,
                        new_password2: str) -> None:

        if new_password1 != new_password2:
            raise Exception("Passwords don't match")

        if not check_password(current_password, self.password):
            raise Exception("Wrong password")

        self.set_password(new_password1)
