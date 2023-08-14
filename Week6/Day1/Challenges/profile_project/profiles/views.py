from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Profile


@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        profile = Profile.objects.create(name=name, email=email)
        return JsonResponse({'success': True})


@csrf_exempt
def delete_profile(request, id):
    if request.method == 'DELETE':
        profile = get_object_or_404(Profile, id=id)
        profile.delete()
        return JsonResponse({'success': True})
