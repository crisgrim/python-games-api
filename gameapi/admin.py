from django.contrib import admin

# Register your models here.
from .models import Game, Party, Message

# Register your models here.
admin.site.register(Game)
admin.site.register(Party)
admin.site.register(Message)
