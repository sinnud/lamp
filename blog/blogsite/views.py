from django.shortcuts import render

# Create your views here.
'''
https://www.digitalocean.com/community/tutorials/how-to-create-django-views

We will keep the import statement that imports the render() function from 
the django.shortcuts library. The render() function allows us to combine 
both a template and a context so that we can return the appropriate 
HttpResponse object. Keep this in mind because with every view we write, 
we are responsible for instantiating, populating, and returning an HttpResponse.

Next we’ll add our first view that will welcome users to the index page. 
We’ll import the HttpResponse() function from the Django http library. 
Using that function, we’ll pass in text to be displayed when the webpage 
is requested. 
'''
from django.http import HttpResponse
from .models import Post

def index(request):
    return HttpResponse('Hello, welcome to the index page.')

'''
Following that, we’ll add one more function that will display the 
individual post we’re going to create later in the tutorial. 
'''
def individual_post(request):
    # return HttpResponse('Hi, this is where an individual post will be.')
    recent_post = Post.objects.get(id__exact=1)
    return HttpResponse(recent_post.title + ': ' + recent_post.content)

'''
Right now, there is no designated URL that these functions are pointing 
to, so we’ll have to add that to our urlpatterns block within our URL 
configuration file. With the views added, let’s move on to mapping URLs 
to them via this configuration file so that we can view the pages we’ve 
created.
'''