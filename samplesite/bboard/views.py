from django.http import HttpResponse
from bboard.models import Bb
from django.template import loader
from django.shortcuts import render

def index(request):
    bbs = Bb.objects.order_by('-published')
    return render(request, 'bboard/index.html', {'bbs': bbs})

    # template = loader.get_template('bboard/index.html')
    # bbs = Bb.objects.order_by('-published')
    # context = {'bbs': bbs}
    # return HttpResponse(template.render(context, request))

    # s = "Список объявление \r\r\r\r"
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(s, content_type='text/plain; charset=utf-8')




