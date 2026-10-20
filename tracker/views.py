from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.views.decorators.http import require_POST

from .models import JobApplication
from .forms import JobApplicationForm


def dashboard(request):
    applications = JobApplication.objects.all()

    selected_status = request.GET.get("status", "")

    valid_statuses = {
        choice[0]
        for choice in JobApplication.STATUS_CHOICES
    }

    if selected_status in valid_statuses:
        applications = applications.filter(
            status=selected_status
        )
    else:
        selected_status = ""

    context = {
        "applications": applications,
        "total_count": JobApplication.objects.count(),
        "applied_count": JobApplication.objects.filter(
            status="Applied"
        ).count(),
        "interview_count": JobApplication.objects.filter(
            status="Interview"
        ).count(),
        "selected_count": JobApplication.objects.filter(
            status="Selected"
        ).count(),
        "rejected_count": JobApplication.objects.filter(
            status="Rejected"
        ).count(),
        "selected_status": selected_status,
        "status_choices": JobApplication.STATUS_CHOICES,
    }

    return render(
        request,
        "tracker/dashboard.html",
        context
    )


def add_application(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = JobApplicationForm()

    return render(
        request,
        "tracker/application_form.html",
        {
            "form": form,
            "page_title": "Add Job Application",
        }
    )


def edit_application(request, pk):
    application = get_object_or_404(
        JobApplication,
        pk=pk
    )

    if request.method == "POST":
        form = JobApplicationForm(
            request.POST,
            instance=application
        )

        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = JobApplicationForm(
            instance=application
        )

    return render(
        request,
        "tracker/application_form.html",
        {
            "form": form,
            "page_title": "Edit Job Application",
        }
    )


def delete_application(request, pk):
    application = get_object_or_404(
        JobApplication,
        pk=pk
    )

    if request.method == "POST":
        application.delete()
        return redirect("dashboard")

    return render(
        request,
        "tracker/confirm_delete.html",
        {"application": application}
    )
