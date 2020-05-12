from django.contrib import admin

# Register your models here.
'''

https://www.digitalocean.com/community/tutorials/how-to-enable-and-connect-the-django-admin-interface

Connecting our blog to the admin will allow us to see links for both 
the Posts and Comments inside the admin dashboard. As we’ve seen 
before, the dashboard currently just displays links for Groups and Users.

To do this, we need to register our Posts and Comments models inside 
of the admin file of blogsite. 
'''
from blogsite.models import Post
from blogsite.models import Comment


admin.site.register(Post)
admin.site.register(Comment)