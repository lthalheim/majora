from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseBadRequest
from django.db.models import Count
from django.db.models import F

from . import models
def sample_sequence_count_dashboard(request):
    collections = models.BiosourceSamplingProcess.objects.values("collected_by").annotate(Count("collected_by")).order_by("-collected_by__count")
    total_collections = models.BiosourceSamplingProcess.objects.count()

    consensii = models.DigitalResourceArtifact.objects.filter(current_kind="consensus").values(org=F("created__who__profile__institute__name")).annotate(count=Count("org"))
    total_consensii = models.DigitalResourceArtifact.objects.filter(current_kind="consensus").count()

    adm2 = models.BiosourceSamplingProcess.objects.all().values(adm2=F("collection_location_adm2")).annotate(count=Count("adm2")).order_by("adm2")

    return render(request, 'public/special/dashboard.html', {
        "collections": collections,
        "total_collections": total_collections,
        "sequences": consensii,
        "total_sequences": total_consensii,
        "adm2": adm2,
        "n_regions": len(adm2),
    })
