from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseBadRequest
from django.db.models import Count

from . import models
def sample_sequence_count_dashboard(request):
    collections = models.BiosourceSamplingProcess.objects.values("collection_by").order_by().annotate(Count("collection_by"))

    return render(request, 'public/special/dashboard.html', {
        "collections": collections,
    })
