from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

class CustomAccountAdapter(DefaultAccountAdapter):
    # 유저 모델 추가 필드 나타내기
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)
        userimage = data.get("userimage")
        if userimage:
            user.userimage = userimage
        user.save()
        return user