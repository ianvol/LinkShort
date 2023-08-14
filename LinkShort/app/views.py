from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
import string
import random
from django.conf import settings
import hashlib
from django.contrib.auth.decorators import login_required

from .models import URL

def generate_short_url(original_url):
    # Create a hash of the original URL
    hash_object = hashlib.sha256(original_url.encode())
    hash_hex = hash_object.hexdigest()

    # Take the first 8 characters of the hash to create a short URL
    short_url = hash_hex[:8]
    
    return short_url

def index(request):
    context = {}
    context['title'] = 'Link Shortener'
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if long_url:
            user = request.user if request.user.is_authenticated else None
            existing_url = URL.objects.filter(long_url=long_url).first()

            if existing_url:
                context['short_url'] = existing_url.short_url
            else:
                while True:
                    short_url = generate_short_url(long_url)
                    if not URL.objects.filter(short_url=short_url).exists():
                        break

                url = URL(long_url=long_url, short_url=short_url, user=user)
                url.save()
                context['short_url'] = short_url

    return render(request, 'index.html', context)



@login_required
def my_links(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_links = URL.objects.filter(user__id=user_id)
        print(user_links) 
        return render(request, 'my_links.html', {'user_links': user_links})
    else:
        return redirect('login')

#def redirect_to_original_url(request, short_url):
#    try:
#        url = get_object_or_404(URL, short_url=short_url)
#        return redirect(url.long_url, permanent=True)
#    except URL.DoesNotExist:
#        raise Http404("URL does not exist")


#def detail(request, uuid):
#    try:
#        # Assuming UUID is a field in your URL model
#        url = URL.objects.get(uuid=uuid)
#        return HttpResponse("You're looking at URL %s." % url.uuid)
#    except URL.DoesNotExist:
#        raise Http404("URL does not exist")  # Or handle the error as you wish