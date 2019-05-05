from django import forms
from .models import Items,ExchangeItems,Feedback,monia_image

class ItemForm(forms.ModelForm):
    class Meta:
        model=Items
        fields=['item_name','item_price','item_image','item_description','contact_number']


class ExchangeItemForm(forms.ModelForm):
    class Meta:
        model=ExchangeItems
        fields=['exchange_item_name','exchange_item_price','exchange_item_image','exchange_items_description']
        
        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['name','email','phone','message']
        

class given_image_form_monia(forms.ModelForm):
    class Meta:
        model=monia_image
        fields=['image_given_monia']                                                          