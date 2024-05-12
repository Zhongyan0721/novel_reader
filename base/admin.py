from django.contrib import admin

# Register your models here.
from .models import Novel, Topic, Author, Comment

admin.site.register(Novel)
admin.site.register(Topic)
admin.site.register(Author)
admin.site.register(Comment)
