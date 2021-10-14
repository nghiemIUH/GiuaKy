from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
# Create your views here.

class IndexView(LoginRequiredMixin, View):
    login_url = '/user/login/'

    def get(self, request):
        posts = models.Post.objects.all()
        return render(request, 'index.html', {'posts': posts})

    def post(self, request):
        data = request.POST
        content = data['content']
        image = request.FILES['image']
        user = request.user
        post = models.Post.objects.create(
            user=user, content=content, image=image)
        post.save()
        return redirect('/')
