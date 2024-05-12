from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .forms import CustomUserCreationForm
from writers.models import Writer
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

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


class WriterCreate(FormView):
    template_name = 'writers/writer_form.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


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
