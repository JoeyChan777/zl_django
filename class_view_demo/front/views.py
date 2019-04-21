from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.views.generic import ListView


def add_article(request):
    articles = []
    for i in range(102):
        article = Article(title='标题：%s' % i, content='内容：%s' % i)
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse('article added successfully.')


class ArticleListView(ListView):
    model = Article
    template_name = 'front/article_list.html'
    paginate_by = 10
    context_object_name = 'articles'
    ordering = 'create_time'
    page_kwarg = 'P'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListView, self).get_context_data()
        context['username'] = 'cj'
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator, page_obj)
        context.update(pagination_data)
        return context

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number
        num_pages = paginator.num_pages
        left_has_more = False
        right_has_more = False

        if current_page <= around_count+2:
            left_pages = range(1, current_page)
        else:
            left_pages = range(current_page-around_count, current_page)
            left_has_more = True

        if current_page >= num_pages-around_count-1:
            right_pages = range(current_page+1, num_pages+1)
        else:
            right_pages = range(current_page+1, current_page+around_count+1)
            right_has_more = True
        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'num_pages': num_pages,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more
        }

