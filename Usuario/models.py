from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, email,  password, is_staff, is_superuser):
        user = self.model(
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser
        )
        user.set_password(password)
        user.save(using=self.db)
        return user



    def create_user(self, email, password=None):
         return self._create_user(email,password, True, True)

    def create_superuser(self, email, password=None):
        return self._create_user(email, password, True, True)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.email
