from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from media_land.media.models import Media
from .forms import CommentForm, SearchForm
from .models import Like


def index(request):
    media = Media.objects.all()
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        photos = media.filter(description__icontains=search_text)

    if not isinstance(request.user, AnonymousUser):
        media.liked_by_user = Like.objects.filter(user=request.user).exists()
    else:
        media.liked_by_user = False

    context = {
            "all_media": Media,
            "comment_form": CommentForm(),
            'search_form': search_form,
    }

    return render(request, template_name='common/index.html', context=context)


@login_required
def like_button(request, media_id):
    media = Media.objects.get(id=media_id)
    liked_object = Like.objects\
        .filter(to_photo_id=media_id, user=request.user)\
        .first()

    if liked_object:
        liked_object.delete()
    else:
        new_liked_object = Like(to_media=media, user=request.user)
        new_liked_object.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{media_id}')


@login_required
def comment_section(request, media_id):
    if request.method == 'POST':
        media = Media.objects.get(id=media_id)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            # CREATE INSTANCE IN MEMORY, BUT DON'T COMMIT IT TO BASE (STILL NO PHOTO REFERENCE)
            comment_instance = comment_form.save(commit=False)
            comment_instance.to_photo = media
            # NOW COMMIT TO BASE
            comment_instance.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{media_id}')
