from django.db import models


class HowItsWork(models.Model):
    title = models.CharField(max_length=128, help_text="How it's work title")
    description = models.CharField(max_length=255, help_text="How it's work description")

    class Meta:
        verbose_name = "How it's work"

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=255, help_text="FAQ question")
    answer = models.TextField(help_text="FAQ answer")

    class Meta:
        verbose_name = "FAQ"

    def __str__(self):
        return self.question
