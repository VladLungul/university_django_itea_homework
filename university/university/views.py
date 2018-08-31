from django.http import JsonResponse
from django.shortcuts import render
from .forms import Student


def my_index_view(request):
    if request.method == "POST":
        form = Student(request.POST)
        if form.is_valid():
            print(form.data)
            return JsonResponse({"message": "Form was processed"})
        data = {'form': form}
    else:
        data = {'form': Student()}
    return render(request, 'university/index.html', data)