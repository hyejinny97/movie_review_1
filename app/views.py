from atexit import register
from django.shortcuts import render, redirect

from pjt_movie.settings import BASE_DIR
from .models import Review
from random import choice

# 루트페이지
def index(request):
    reviews = Review.objects.all().order_by('-updated_at')
    movie_images = ['https://upload.wikimedia.org/wikipedia/ko/2/23/%EC%BA%90%EC%B9%98_%EB%AF%B8_%EC%9D%B4%ED%94%84_%EC%9C%A0_%EC%BA%94_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg','https://t1.daumcdn.net/movie/36f22dea0e0a9e0e626c549ce689558160c46ed4','https://t1.daumcdn.net/movie/ec835362c051a621cda0411af5a61a20464a161b']
    images=[]
    for i in range(len(reviews)):
        images.append(choice(movie_images))

    context ={
        'movie_img': images,
        'reviews': reviews,
    }
    
    return render(request,"app/index.html", context)



# 글 작성 페이지
def new(request):
    
    return render(request,"app/new.html")



# 글 작성 후 저장
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    star_point = request.GET.get('reviewStar')

    review = Review(title=title, content=content, star_point=star_point)
    review.save()

    return redirect('app:detail', review.pk)



# 글 자세히 페이지
def detail(request, review_pk):
    review = Review.objects.get(id=review_pk)

    context = {
        'review': review,
    }

    return render(request, 'app/detail.html', context)



# 수정 페이지
def edit(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    context = {
        'review' : review,
    }

    return render(request, 'app/edit.html', context)



# 글 수정 후 디테일 페이지
def update(request, review_pk):
    title = request.GET.get('title')
    content = request.GET.get('content')
    star_point = request.GET.get('reviewStar')

    review = Review.objects.get(pk=review_pk)
    review.title = title
    review.content = content
    review.star_point = star_point
    review.save()

    return redirect('app:detail', review.pk)



# 글 삭제
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    review.delete()

    return redirect('app:index')