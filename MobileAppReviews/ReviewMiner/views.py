#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response

from ReviewMiner import reviewsProcessing

# Create your views here.
def appReview(request):
    template = loader.get_template('ReviewMiner/Home.html')
    context = RequestContext(request)
    return HttpResponse(template._render(context))


def appReviewUploadDone(request):
    #https://docs.djangoproject.com/en/1.7/topics/http/file-uploads/
    if request.method == 'POST':

        file1 = request.FILES['file']

        with open('uploaded_files/ReviewMiner/test1.csv', 'wb+') as destination:
            for chunk in file1.chunks():
                destination.write(chunk)

        allReviews = reviewsProcessing.getprocessedreviews()

        return render(request, 'ReviewMiner/Output.html', {'allReviews': allReviews})
    return render_to_response('ReviewMiner/Home.html')