from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
import string
import random
from django.conf import settings


from .models import URL

def index(request):
    context = {}
    context['title'] = 'Link Shortener'
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if long_url:
            short_url = generate_short_url()
            url = URL(long_url=long_url, short_url=short_url)
            url.save()
            context['short_url'] = short_url
    return render(request, 'index.html', context)

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    return f'{settings.DOMAIN_NAME}/{short_url}'

#def redirect_to_long_url(request, short_url):
#    try:
#        url = URL.objects.get(short_url=short_url)
#        return redirect(url.long_url)
#    except URL.DoesNotExist:
#        raise Http404("URL does not exist")  # Or handle the error as you wish

#def detail(request, uuid):
#    try:
#        # Assuming UUID is a field in your URL model
#        url = URL.objects.get(uuid=uuid)
#        return HttpResponse("You're looking at URL %s." % url.uuid)
#    except URL.DoesNotExist:
#        raise Http404("URL does not exist")  # Or handle the error as you wish