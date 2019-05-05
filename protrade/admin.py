from django.contrib import admin
from .models import Items,ExchangeItems,Feedback,monia_image,image_name_monia,predicted_label

# Register your models here.
admin.site.register(Items)
admin.site.register(ExchangeItems)
admin.site.register(Feedback)

admin.site.register(monia_image)
admin.site.register(image_name_monia)
admin.site.register(predicted_label)
