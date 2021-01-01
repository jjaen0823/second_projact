from django.contrib import admin
from .models import Blog  # 동일한 폴더위치에 있는 models 라는 파일에, Blog 라는 클래스를 가져오라


# Register your models here.

# 'admin/' site에 Blog 라는 클래스를 등록
admin.site.register(Blog)