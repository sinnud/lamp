from django.db import models

# Create your models here.
''' 

https://www.digitalocean.com/community/tutorials/how-to-create-django-models

Within this file, the code to import the models API is already added, 
we can go ahead and delete the comment that follows. Then we’ll 
import slugify for generating slugs from strings, Django’s User 
for authentication, and reverse from django.urls to give us greater 
flexibility with creating URLs. 
'''
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

'''
Then, add the class method on the model class we will be calling Post, 
with the following database fields, title, slug, content, created_on 
and author. Add these below your import statements.
'''
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

    '''
    Next, we will add functionality for the generation of the URL and 
    the function for saving the post. This is crucial, because this 
    creates a unique link to match our unique post.
    '''
    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    '''
    Now, we need to tell the model how the posts should be ordered, 
    and displayed on the web page. The logic for this will be added 
    to a nested inner Meta class. The Meta class generally contains 
    other important model logic that isn’t related to database field 
    definition.
    '''
    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title

'''
Finally, we will add the Comment model to this file. This involves 
adding another class named Comment with models.Models in its 
signature and the following database fields defined:

    name — The name of the person posting the comment.
    email — The email address of the person posting the comment.
    text — The text of the comment itself.
    post — The post with which the comment was made.
    created_on — The time the comment was created.

'''
class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

'''
At this point models.py will be complete. Ensure that 
your models.py file matches the following:
'''