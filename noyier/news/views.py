from django.template import RequestContext, Context, loader
from news.models import News
from django.http import HttpResponse

def index(request):
    news = News.objects.all()
    t = loader.get_template('news/index.html')
    c = RequestContext(request,	{
        'news':news,
    })
    return HttpResponse(t.render(c))

def detail(request, news_id):
	new = News.objects.get(pk = news_id)
	path = new.image.path.split('/').pop()
	t = loader.get_template('news/detail.html')
	c = RequestContext(request, {
		'new' : new, 'path': path,
	})
	return HttpResponse(t.render(c))
	
