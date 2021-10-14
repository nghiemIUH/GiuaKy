from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars

# Create your models here.


class CustomUser(AbstractUser):

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField(blank=True,
                               upload_to='avatars')

    def __str__(self):
        return self.username
