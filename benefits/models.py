from django.db import models

MONTH_CHOICES = [
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
]


class BoostSales(models.Model):
    month = models.CharField(
        max_length=2,
        choices=MONTH_CHOICES,
        help_text="Month (without year)"
    )
    sales_qnt = models.PositiveIntegerField(help_text="Number of sales per month", default=0)
    is_active_updating_the_photo_menu = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Boost Sales"

    def __str__(self):
        return self.get_month_display()


class UpperBanner(models.Model):
    title = models.CharField(max_length=255, help_text="Benefits upper banner description")
    description = models.CharField(max_length=255, help_text="Benefits upper banner description")
    image = models.ImageField(upload_to='images/benefits/', help_text="Benefits upper banner image")

    class Meta:
        verbose_name = "The upper banner"

    def __str__(self):
        return self.title


class LowerBanner(models.Model):
    title = models.CharField(max_length=255, help_text="Benefits lower banner description")
    description = models.CharField(max_length=255, help_text="Benefits lower banner description")
    image = models.ImageField(upload_to='images/benefits/', help_text="Benefits lower banner image")

    class Meta:
        verbose_name = "The lower banner"

    def __str__(self):
        return self.title

