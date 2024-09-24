from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReportsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "project.apps.reports"
    verbose_name = _("Reports")

    def ready(self) -> None:
        import project.apps.reports.signals
