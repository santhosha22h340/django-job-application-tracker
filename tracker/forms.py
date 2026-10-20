from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = [
            "company",
            "role",
            "location",
            "job_url",
            "applied_date",
            "status",
            "notes",
        ]

        widgets = {
            "applied_date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "notes": forms.Textarea(
                attrs={"rows": 3}
            ),
        }

        labels = {
            "company": "Company Name",
            "role": "Job Role",
            "location": "Location",
            "job_url": "Job Posting URL",
            "applied_date": "Application Date",
            "status": "Application Status",
            "notes": "Notes",
        }