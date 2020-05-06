from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from console.models import Console
from django.shortcuts import redirect


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        consoles = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'firstImage': x.consoleimage_set.first().image
        } for x in Console.objects.filter(name__icontains=search_filter)]
        # TODO: Exception handling, No results.
        # TODO: Find a way to make Json Response format into a different HTML file, not index.html
        return JsonResponse({'data': consoles})
        # result = {'search_result': consoles}
        # return redirect('')     # render(request, 'console/filterindex.html', result)

    context = {'nintendo': Console.objects.filter(brand_id=1).order_by('name'),
               'microsoft': Console.objects.filter(brand_id=2).order_by('name'),
               'sony': Console.objects.filter(brand_id=3).order_by('name'),
               'sega': Console.objects.filter(brand_id=4).order_by('name')
               }
    return render(request, 'console/index.html', context)


# def get_consoles_by_brand(request, brand):
#
#     print(brand, 'getting consoles!')
#     return render(request, 'console/filterindex.html', {'consoles': []})
#
#
# def get_consoles_by_type(request, type):
#     print(type, 'getting by types')
#     return render(request, 'console/filterindex.html', {'consoles': []})


def get_consoles_by_group(request):
    path = request.path

    group = path.strip().split('/')[2]

    if group == 'nintendo':
        context = {'consoles': Console.objects.filter(brand_id=1).order_by('name'),
                   'group': 'Nintendo'}
    elif group == 'microsoft':
        context = {'consoles': Console.objects.filter(brand_id=2).order_by('name'),
                   'group': 'Microsoft'}
    elif group == 'sony':
        context = {'consoles': Console.objects.filter(brand_id=3).order_by('name'),
                   'group': 'Sony'}
    elif group == 'sega':
        context = {'consoles': Console.objects.filter(brand_id=4).order_by('name'),
                   'group': 'SEGA'}
    elif group == 'handheld':
        context = {'consoles': Console.objects.filter(category_id=1),
                   'group': 'Handheld'}
    elif group == 'home_consoles':
        context = {'consoles': Console.objects.filter(category_id=2),
                   'group': 'Home Consoles'}
    # else:
    #     # TODO: Error handling, category does not exist, url not mapped.

    return render(request, 'console/filterindex.html', context)



def get_console_by_id(request, id):
    return render(request, 'console/console_details.html', {
        'console': get_object_or_404(Console, pk=id)
    })
