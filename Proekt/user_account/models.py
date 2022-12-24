from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MinValueValidator
from datetime import datetime, timedelta


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Супер пользователь должен быть назначен is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Супер пользователь должен быть назначен is_superuser=True')

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError(_('Вы должны предоставить почту.'))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)

        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    SUBSCRIBE_CHOISE = (
        ("DEFAULT", "DEFAULT"),
        ("BASIC", "BASIC"),
        ("PREMIUM", "PREMIUM")

    )
    email = models.EmailField(_('почта'), unique=True)
    balance = models.PositiveBigIntegerField(_('баланс'), default=0)
    subscribe = models.CharField(_('тип подписки'), choices=SUBSCRIBE_CHOISE, default="DEFAULT", max_length=7)
    subscribe_date = models.DateField(_('подписка до'), default=timezone.now())
    now=datetime.now()
    start_date = models.DateTimeField(_('дата регистрации'), default=timezone.now())
    user_image = models.ImageField(_('фото профиля'), upload_to='profile_image/', default='profile_image/user.png')
    is_staff = models.BooleanField(_('staff'),default=False)
    is_active = models.BooleanField(_('активный'),default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class CheckPayment(models.Model):
    email = models.CharField(_('почта'), max_length=25)
    bill_id = models.CharField(_('bill_id'), max_length=100)
    comment = models.CharField(_('коментарий'), max_length=100)
    amount = models.IntegerField(_('сумма пополнения'), default=0, validators=[MinValueValidator(100)])

    def __str__(self):
        return self.email


    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

class Course(models.Model):
    SUBSCRIBE_CHOISE = (
        ("BASIC", "BASIC"),
        ("PREMIUM", "PREMIUM")

    )
    name= models.CharField(_('название'), max_length=25)
    tou = models.TextField(_('описание'), max_length=100)
    file = models.FileField(_('файл курса'), upload_to='course/', blank=True)
    date = models.DateTimeField(_('дата курса'), default=timezone.now())
    subscribe_type = models.CharField(_('тип подписки'), choices=SUBSCRIBE_CHOISE, default="DEFAULT", max_length=7)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'