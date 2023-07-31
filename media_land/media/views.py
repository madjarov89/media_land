from django.shortcuts import render


def media_details(request):
    return render(request, template_name='media/media-details.html')


def add_media(request):
    return render(request, template_name='media/add-media.html')


def edit_media(request):
    return render(request, template_name='media/edit-media.html')


def delete_media(request):
    return render(request, template_name='media/delete-media.html')
