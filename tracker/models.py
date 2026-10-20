from django.db import models
from django.utils import timezone


class JobApplication(models.Model):

    STATUS_CHOICES = [
        ("Applied", "Applied"),
        ("Interview", "Interview"),
        ("Selected", "Selected"),
        ("Rejected", "Rejected"),
    ]

    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    location = models.CharField(
        max_length=100,
        blank=True
    )

    job_url = models.URLField(blank=True)

    applied_date = models.DateField(
        default=timezone.localdate
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Applied"
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.company} - {self.role}"

    class Meta:
        ordering = ["-applied_date", "-id"]
