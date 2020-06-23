from django.views import View
from .models import Plant,Leaf,Flower
from django.http import HttpResponse
from django.shortcuts import render

class LookView(View):
        def get(self, request):
                return render(request, 'index.html')

        def post(self, request):
                leaf_names = request.POST.getlist('leaf_name')
                results = []
                for leaf_name in leaf_names:
                        result = Plant.objects.filter(leafchars__chars=leaf_name)
                        if results is not []:
                                results = list(set(result) & (set(results)))
                        else:
                                results.append(result)
                print(results)
                return HttpResponse('success')
                # return render(request, 'index2.html', context={'results': results})
