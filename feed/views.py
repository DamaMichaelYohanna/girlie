

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet, TweetImage
from .forms import TweetForm

@login_required
def post_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()

            # Handle multiple images
            images = request.FILES.getlist('images')
            for image in images:
                TweetImage.objects.create(tweet=tweet, image=image)

            return redirect('home')
    else:
        form = TweetForm()
    return render(request, 'tweets/post_tweet.html', {'form': form})
