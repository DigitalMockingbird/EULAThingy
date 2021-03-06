from django.db import models


class ThingyDoc(models.Model):
    title = models.CharField(
        max_length=250, null=False, blank=False,
        verbose_name='Document title.'
    )
    rating = models.IntegerField(
        null=False, blank=False, default=0, db_index=True
    )
    votes = models.IntegerField(
        null=False, blank=False, default=0
    )
    category_choices = (
        (0, 'Other'),
        (1, 'Health'),
        (2, 'Technology'),
        (3, 'Finance'),
        (4, 'Service')
    )
    category = models.IntegerField(
        choices=category_choices, null=False,
        blank=False, db_index=True, default=0
    )
    last_modified = models.DateTimeField(
        auto_now_add=True, null=False, blank=False
    )
    uploaded = models.DateTimeField(
        auto_now_add=True, null=False, blank=False
    )


class ThingyString(models.Model):
    doc = models.ForeignKey(
        ThingyDoc
    )
    string = models.TextField(
        null=False, blank=False
    )
    rating = models.IntegerField(
        null=True, blank=False, default=0
    )
    votes = models.IntegerField(
        null=False, blank=False, default=0
    )
    last_updated = models.DateTimeField(
        auto_now=True, null=False, blank=False, db_index=True
    )
