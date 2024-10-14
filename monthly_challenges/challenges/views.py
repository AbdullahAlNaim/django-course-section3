from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'january': 'exercise daily',
    'february': 'eat clean daily',
    'march': 'run 1 mile a day',
    'april': 'rank up in valorant',
    'may': 'get a job',
    'june': 'buy a car',
    'july': 'buy a house',
    'august': 'build an application',
    'september': 'Start a company',
    'october': 'Get married',
    'november': 'Visit tokyo',
    'december': None
}

# Create your views here.

def index(request):
    # list_items = ''
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {
        'months': months
    })

    # replaced this with django shortcut render method 
    # response_data = f"""
    #     <ul>
    #         {list_items}
    #     </ul>
    # """
    # return HttpResponse(response_data)

def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid Month')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            "month": month,
            "challenge": challenge_text
        })

        # replaced this with django shortcut render method 
        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
    except:
        raise Http404()
    