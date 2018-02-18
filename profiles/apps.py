from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProfilesConfig(AppConfig):
    name = 'profiles'
    verbose_name = _('Profile')
    verbose_name_plural = _('Profiles')
