from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView

from writers.models import Writer

def index(request):
    writers_qty = Writer.objects.count()  # db level -> COUNT()
    writers = Writer.objects.all()

    context = {
        'writers': writers,
        'writers_qty': writers_qty,
        'endpoint': request.resolver_match.view_name,
    }

    return render(request, 'writers/index.html', context=context)


class PageTitleMixin:
    page_title = 'V-Blog'

    # def dispatch(self):
    #     pass

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # print(f'{context=}')
        context['page_title'] = self.page_title

        return context
    

class WritersList(PageTitleMixin, ListView):
    page_title = 'Writers'
    model = Writer
    paginate_by = 2


class WriterCreate(CreateView):
    model = Writer
    fields = '__all__'
    # form_class = ...
    # success_url = ...
    success_url = '/'


class WriterDetail(PageTitleMixin, DetailView):
    page_title = 'Writer page'
    model = Writer
    # template_name = 'animals/animal.html'
    # template_name_suffix = '_info'

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs.order_by('-id')
    #     return qs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     # print(f'{context=}')
    #     context['page_title'] = 'Animal page'
    #
    #     return context
