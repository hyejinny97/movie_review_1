from django.shortcuts import render, redirect
from .models import Review



# 루트페이지
def index(request):
    reviews = Review.objects.all()

    context ={
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

    review = Review(title=title, content=content)
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

    review = Review.objects.get(pk=review_pk)
    review.title = title
    review.content = content
    review.save()

    return redirect('app:detail', review.pk)



# 글 삭제
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    review.delete()

    return redirect('app:index')