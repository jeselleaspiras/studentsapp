from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Student
from .forms import PostForm, StudentForm

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404


def post_list(request):
    posts = Post.objects.filter()
    return render(request, 'post_list.html', {'posts': posts})

def student_list(request):
    students = Student.objects.filter()
    return render(request, 'student_list.html', {'students': students})

def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': posts})

def post_create(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        # message success
        #messages.success(request, "Successfully Created")
        return redirect('post_detail', pk=post.pk)
    else:
        return render(request, 'post_edit.html', {'form': form})

def student_create(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    form = StudentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        student = form.save(commit=False)
        student.user = request.user
        student.save()
        # message success
        #messages.success(request, "Successfully Created")
        return redirect('/students/accounts', pk=student.pk)
    else:
        return render(request, 'student_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('/students/accounts', pk=pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_edit.html', {'form': form})

def post_delete(request, pk=None):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	instance = get_object_or_404(Post, pk=pk)
	instance.delete()
	messages.success(request, "Successfully deleted")
        return redirect('/students')

def student_delete(request, pk=None):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	instance = get_object_or_404(Student, pk=pk)
	instance.delete()
	messages.success(request, "Successfully deleted")
        return redirect('/students/accounts')