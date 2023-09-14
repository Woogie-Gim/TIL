from django.contrib import admin
# 명시적 상대 경로
from .models import Article

# Register your models here.
# Article 모델 클래스를 admin site에 등록하는 과정
# admin site에 등록한다(register).
admin.site.register(Article)

