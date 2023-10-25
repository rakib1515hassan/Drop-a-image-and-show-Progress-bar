from django.shortcuts import render
from .models import ImageUpload
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def test_view(request):
    # if request.method == 'post':
    #     title  = request.POST.get('uplode_title')
    #     pic    = request.Files.get('uplode_image')

    #     print("---------------------------")
    #     print("Title is ", title)
    #     print("Pic is ", pic)
    #     print("---------------------------")

    #     ImageUpload.objects.create(
    #         title=title, 
    #         pic=pic
    #         )

    return render(request, 'home2.html')


@csrf_exempt  # Disable CSRF protection for this view (only for demonstration, not recommended in production)
def upload_image(request):
    if request.method == 'POST':
        title = request.POST.get('uplode_title')
        image = request.FILES.get('uplode_image')

        if title and image:
            instance = ImageUpload(title=title, image=image)
            instance.save()

            return JsonResponse({'message': 'Image uploaded successfully'})

    return JsonResponse({'error': 'Invalid request'})
