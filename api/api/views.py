from django.http import JsonResponse
from django.utils.translation import gettext as _


def index(request): 
    output = _("Welcome to my site.")
    print(output)
    return JsonResponse({"test": output})
    