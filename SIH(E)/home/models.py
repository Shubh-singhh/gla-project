from django.db import models
# from django.template.defaultfilters import truncatechars 
# from django.utils.safestring import mark_safe

class Note(models.Model):
    userr = models.CharField(max_length=30)
    uemail = models.CharField(max_length=20)
    ucomment = models.TextField()
    
    def __str__(self):
        return self.title

class DemoModel(models.Model):
    okmail = models.CharField(max_length=20)
    addr = models.CharField(max_length=70)
    comment = models.CharField(max_length=70)
    num = models.CharField(max_length=12)
    cause_image = models.ImageField(null=True,blank=True,upload_to="demo",default=None)
    
    # @property
    # def short_description(self):
    #     return truncatechars(self.description, 20)

    # def admin_photo(self):
    #     return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
    # admin_photo.short_description = 'Image'
    # admin_photo.allow_tags = True

    def __str__(self):
        return self.title