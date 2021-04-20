from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "csi_localhost.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import csi_localhost.users.signals  # noqa F401
        except ImportError:
            pass
