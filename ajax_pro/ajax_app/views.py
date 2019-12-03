from django.shortcuts import render
from django.views.generic import ListView, View
from .models import CurdUser
from django.http import JsonResponse


class CurdView(ListView):
    model = CurdUser
    template_name = 'ajax_app/curd.html'
    context_object_name = 'users'


class CreateCrudUser(View):
    def get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CurdUser.objects.create(
            name=name1,
            address=address1,
            age=age1
        )
        user = {'id': obj.id, 'name': obj.name, 'address': obj.address, 'age': obj.age}

        data = {
            'user': user
        }

        return JsonResponse(data)


class UpdateCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CurdUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id': obj.id, 'name': obj.name, 'address': obj.address, 'age': obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)


class DeleteCrudView(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        CurdUser.objects.Get.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)