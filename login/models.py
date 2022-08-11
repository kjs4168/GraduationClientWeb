from django.db import models

# Create your models here.
class CloudUser(models.Model):
    name = models.TextField()
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #모델을 통해 생성할 때 생성 시각이 자동으로 입력되게
    updated_at = models.DateTimeField(auto_now=True)    #모델을 통해 업데이트할 때 수정 시각이 자동으로 입력되게 

    def __str__(self):  #java의 toString과 같은 느낌
        return self.name
