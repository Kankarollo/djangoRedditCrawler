from django.shortcuts import render
from praw.reddit import Subreddit
from utils.reddit_crawler import RedditCrawler
from .forms import SearchForm
from .models import RedditSubreddit

def home(request):
    posts = []
    subreddit = RedditSubreddit.objects.first()
    print(f"subreddit = {subreddit}")
    if subreddit is None:
        for index in range(1,4):
            posts.append({"author": f"author {index}", "title": f"Lorem Ipsum part {index}", "score":f"date{index}", "url":"None"})
    else:
        posts = RedditCrawler.get_posts_data(subreddit.name)
    context = {
        'posts': posts
    }
    return render(request, 'menu/menuPage.html', context=context)

def search_reddit_page(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        searched_subreddit = request.POST['subreddit_name']
        if RedditSubreddit.objects.all().count() > 1:
            subreddit = RedditSubreddit.objects.first()
        else:
            subreddit = RedditSubreddit()
        if RedditCrawler.sub_exists(searched_subreddit):
            subreddit.name = searched_subreddit
            subreddit.save()
        posts = RedditCrawler.get_posts_data(subreddit.name)
        if form.is_valid():
            print(f"[INFO] Searched subreddit = {searched_subreddit}")
        else:
            print("[ERROR] FORM IS NOT VALID! SOMETHING WRONG WITH ENTERED QUERY!")
    else:
        form = SearchForm()
    context = {
        'posts': posts
    }
    return render(request, 'menu/menuPage.html', context={'posts': posts, 'form':form})