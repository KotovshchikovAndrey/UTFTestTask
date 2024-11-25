from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        editable=False,
        verbose_name="Дата создания",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False,
        editable=False,
        verbose_name="Дата обновления",
    )

    class Meta:
        abstract = True
