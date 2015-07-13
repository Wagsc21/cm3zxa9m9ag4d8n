
from django import forms
from .models import *
from datetime import datetime
from django.shortcuts import get_object_or_404
class QueryForm(forms.ModelForm):

	class Meta:
		model = Query
		fields = ('title','details')
		#write fields = ('title','details','pub_date','thumbnail') to include thumbnails
	#----------------------------------------------------------------------
	def save(self,request,commit=True):
		userform=super(forms.ModelForm,self).save(commit=False)
		userform.user=request.user
		userform.pub_date=datetime.now()
		if commit:
			userform.save()
			return userform
		
		
		
class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('name','body')
	def save(self,request,query_id,commit=True):
		userform=super(forms.ModelForm,self).save(commit=False)
		userform.user=request.user
		userform.pub_date=datetime.now()
		userform.query=get_object_or_404(Query,id=query_id)
		if commit:
			userform.save()
			return userform	


class NotificationForm(forms.ModelForm):

	class Meta:
		model = Notification
		fields = ()

