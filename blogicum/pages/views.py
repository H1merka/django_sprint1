from django.shortcuts import render


# Create your views here.
def rules(request):
    template_name = 'pages/rules.html'
    return render(request, template_name)


def about(request):
    template_name = 'pages/about.html'
    return render(request, template_name)
