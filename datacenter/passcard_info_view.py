from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404, get_list_or_404

def passcard_info_view(request, passcode):

    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = get_list_or_404(Visit, passcard=passcard)

    this_passcard_visits = []
    for visit in passcard_visits:
        the_visit = {
            'entered_at': visit.entered_at,
            'duration': visit.get_duration(),
            'is_strange': visit.is_strange(),
        }
        this_passcard_visits.append(the_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
