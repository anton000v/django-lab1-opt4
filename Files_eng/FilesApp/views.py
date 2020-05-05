from django.shortcuts import render
from django.views import View
from .models import File
from django.http import JsonResponse

class Index(View):
    def get(self, request):
        all_files = File.objects.all()
        context = {
            'all_files' : all_files,
        }
        return render(request, 'FilesApp/index.html', context = context)

class AjaxAddDownload(View):
    def get(self, request):
        if request.is_ajax():
            id = request.GET.get('id')
            up_file = File.objects.get(id=id)
            up_file.add_download()
            up_file.save()
            return JsonResponse({'message':'Success'})
        else:
            raise 404

class AdminStatistics(View):
    def get(self, request):
        if request.user.is_superuser:
            all_files = File.objects.all()
            context = {
                'all_files':all_files,
            }
            return render(request,'FilesApp/admin-stat.html', context=context)
        else:
            raise 404