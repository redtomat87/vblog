from django.shortcuts import render
from writers.models import Writer
# Create your views here.

def index(request):
    writers_qty = Writer.objects.count()  # db level -> COUNT()
    writers = Writer.objects.all()

    context = {
        'writers': writers,
        'writers_qty': writers_qty,
    }

    return render(request, 'writers/index.html', context=context)
