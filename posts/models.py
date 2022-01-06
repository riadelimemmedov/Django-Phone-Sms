from django.db import models
from users.models import CustomUser#Yeni hemim istifadecini cek
import random
# Create your models here.

class Code(models.Model):
    number = models.CharField(max_length=255,blank=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)#yeni CustomUserden gelen istifadeci
    
    def __str__(self):
        return self.number


#!Bu, veritabanına bir girdi kaydedilmeden önce veya sonra çalıştırılması gereken herhangi bir eylemi gerçekleştirmek istendiğinde, bu, kaydetme yöntemini geçersiz kılarak ve eylemleri gerçekleştirerek gerçekleştirilebileceği anlamına gelir.
    def save(self, *args, **kwargs):#yeni post avtomtik save olanda bu kodlar islesin
        number_list = [x for x in range(10)]#1-araliginindaki deyerleri getirir bize
        code_items = []
        
        for i in range(5):#yeni 5 qeder dovr donsun 5 defe 0 daxil olmagla her dovrde random bir reqem seccsin number_listden
            num  = random.choice(number_list)
            code_items.append(num)
            
        code_string = ''.join(str(item) for item in code_items)#sonra listedeki deyerlerin hamsi biri-birine yapisacag
        self.number = code_string#axirdada bu 5 reqemli deyeri self.number gonder
        
        super().save(*args, **kwargs)
