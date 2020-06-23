import builtins
from builtins import list, set, print, len

from django.views import View
from .models import Plant, Leaf, Flower
from django.shortcuts import render


class LookView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        leaf_names = request.POST.getlist('leaf_name')
        results = []
        for leaf_name in leaf_names:
            result = Plant.objects.filter(leafchars__chars=leaf_name)
            if len(results):
                results = list(set(result) & set(results))
            else:
                results = result
        print(results)
        return render(request, 'index.html', context={'results': results})
