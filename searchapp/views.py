from django.shortcuts import render
from django.db.models import Q
from . models import StudentInfo

# Create your views here.

def homepage(request):
    data = StudentInfo.objects.all()
    return render(request, 'homepage.html', {'data':data})


def SearchPage(request):
    data= ""
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_query = Q(Q(name__icontains=q) | Q(level__icontains=q) | Q(subject__icontains=q))
        data = StudentInfo.objects.filter(multiple_query)
        return render(request, 'searchpage.html', {'data':data, 'q':q})
    else:
        pass
    return render(request, 'searchpage.html', {})



