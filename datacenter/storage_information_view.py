from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_list_or_404


def storage_information_view(request):
    non_closed_visits = []
    inside = get_list_or_404(Visit, leaved_at__isnull=True)
    for visit in inside:
        the_visit = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': visit.get_duration,
        }
        non_closed_visits.append(the_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
