from django.contrib import admin
from .models import Story, StoryComment, StroyPicture

admin.site.register(Story)
admin.site.register(StroyPicture)
### 댓글 기능 추가 ### 2022.08.10
admin.site.register(StoryComment)