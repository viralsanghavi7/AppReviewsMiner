from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader





def index(request):
    template = loader.get_template('myapp/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))



