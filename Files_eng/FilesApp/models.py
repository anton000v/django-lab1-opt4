from django.db import models

class File(models.Model):
    title = models.CharField(max_length = 150, verbose_name='Описание')
    up_file = models.FileField(max_length = 100, verbose_name='Файл')
    download_counter = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

    def add_download(self):
        self.download_counter +=1
        # return self.download_counter

    
    
    
