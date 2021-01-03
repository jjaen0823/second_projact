from django.db import models

# Create your models here.

class Blog(models.Model): # db 수정하면 migrate 다시하기!!
    # title, pub_date, body는 모델의 속성들
    # 여기 적은 내용이 admin 페이지에서 add blog 페이지의 양식을 결정
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')  # date, time
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]