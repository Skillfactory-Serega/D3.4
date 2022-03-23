from datetime import datetime

from django.views.generic import  ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'postALL.html'
    context_object_name = 'postALL'
    queryset = Post.objects.order_by('-dateCreation')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'