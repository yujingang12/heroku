from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
#상속페이지
def layout(request):
    return render(request, 'herokuApp/layout.html')

#메인페이지
def main(request):
    posts = Post.objects
    return render(request, 'herokuApp/main.html', {'posts':posts})

#글 내용 페이지
def detail(request, id):
    post = get_object_or_404(Post, id = id)
    return render(request, 'herokuApp/detail.html', {'post':post})

#글쓰기 페이지
def new(request):
    return render(request, 'herokuApp/new.html')

#글쓰기 함수
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('main')
    else:
        form = PostForm()
        return render(request, 'herokuApp/new.html', {'form':form})

#수정페이지
def edit(request, id):
    edit_post = Post.objects.get(id = id)
    return render(request, 'herokuApp/edit.html', {'post':edit_post})

#수정 함수
def update(request, id):
    update_post = Post.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('detail', update_post.id)

#삭제
def delete(request, id):
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('main')