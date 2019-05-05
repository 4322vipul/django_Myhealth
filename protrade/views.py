from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .models import Items,ExchangeItems,Feedback,monia_image,image_name_monia,predicted_label
from .forms import ItemForm,ExchangeItemForm,FeedbackForm,given_image_form_monia
from django.conf import settings
from keras.preprocessing import image
from keras.models import model_from_json

import cv2
from PIL import Image
import numpy as np
import pandas as pd
import os.path

# Create your views here.

def login_view(request):
    username=password=''
    username=request.POST.get("username")
    password=request.POST.get("password")
    user=authenticate(request,username=username,password=password)
    
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse("home"))
 
    else:
        return render(request,"protrade/login.html",{"message":"Invalid Credentials"})
    
    
    
def home(request):
    
    return render(request,"protrade/home.html")
'''
    if not request.user.is_authenticated:
        return render(request,"protrade/login.html",{"message":None})
    context={"user":request.user}
'''    
    
   

def buy(request):
    
    form=given_image_form_monia(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        
        a=form.cleaned_data['image_given_monia']
        name=image_name_monia(name_of_image_monia=a)
        name.save()
        b=image_name_monia.objects.all().last()
        print(b)
        c=str(b)
        new_path=os.path.join('/home/vipul/Django_test/media/',c)
        print(new_path)
        
        img=image.load_img(new_path,target_size=(64,64))
        print(img)
        
        arr=np.array(img)
        print(arr.shape)
        
        img=image.img_to_array(img)
        img=np.expand_dims(img,axis=0)
        
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("model.h5")
        
        result=loaded_model.predict(img)
        #training_set.class_indices
        if result[0][0]==1:
            prediction='Normal'
        else:
            prediction='Pneumonia'

        print('The given picture is',prediction) 
        label_pred=predicted_label(label=prediction)
        label_pred.save()
        
        name=predicted_label.objects.all().last()
        context={"name":name}
        
        return render(request,'protrade/successPage.html',context)
 
    context={'form':form}
    return render(request,"protrade/buy.html",context)

def sell(request):

    form=ItemForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        #item=Items.objects.all()
        #context={"item":item}
        return render(request,'protrade/successPage.html')
    context={'form':form}
    
    return render(request,'protrade/sell.html',context)
   
def successPage(request):
    
    return render(request,'successPage.html')


def swap(request):
    form=ExchangeItemForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
                
        a=form.cleaned_data['exchange_item_price']

        item=Items.objects.filter(item_price=a).all()
        b=Items.objects.filter(item_price=a).all().count()
        context={"item":item}
        if b==0:
            return render(request,"protrade/validItems.html",{"message":"Sorry no item found with similar price!!"})
        else:
            return render(request,"protrade/validItems.html",context)
        
        
    context={'form':form}    
    return render(request,"protrade/swap.html",context)
        
def contacts(request):
    form=FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request,'protrade/feedbackSuccessPage.html')
    
    context={'form':form}     
    return render(request,"protrade/contacts.html",context)

def feedbackSuccessPage(request):
    return render(request,'feedbackSuccessPage.html')

def logout_view(request):
    logout(request)
    return render(request,"protrade/login.html",{"message":"Logged Out."})