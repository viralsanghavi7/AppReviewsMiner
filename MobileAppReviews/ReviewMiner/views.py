#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response

from ReviewMiner.reviewsProcessing import ReviewsProcessing


# Create your views here.
def appReview(request):
    template = loader.get_template('ReviewMiner/Home.html')
    context = RequestContext(request)
    return HttpResponse(template._render(context))


def appReviewUploadDone(request):
    #https://docs.djangoproject.com/en/1.7/topics/http/file-uploads/
    if request.method == 'POST':

        if 'file' in request.FILES:
            file1 = request.FILES['file']
            with open('uploaded_files/ReviewMiner/Test2.csv', 'wb+') as destination:
                for chunk in file1.chunks():
                    destination.write(chunk)
            callingClass = ReviewsProcessing()
            allReviews, allIndividualReviews = callingClass.getprocessedreviews()
            totalList = []
            print(len(allIndividualReviews))
            totalList.append(allReviews)
            totalList.append(allIndividualReviews)

            return render(request, 'ReviewMiner/Output.html', {'totalList':totalList})

        return render_to_response('ReviewMiner/Home.html')

def about(request):
    template = loader.get_template('ReviewMiner/About.html')
    context = RequestContext(request)
    return HttpResponse(template._render(context))