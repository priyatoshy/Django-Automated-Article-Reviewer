from django.forms import ModelForm
from django import forms 
from models import Article

class ArticleForm(ModelForm):

    class Meta:
        model=Article
        #exclude =['voted']
        #exclude = ()
        #fields="__all__"
        fields=['topic','content']
        #adding widgets
      
  
     
   

     
    #adding classes through method overriding
    def __init__(self,*args, **kwargs):
        super(ArticleForm,self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {'class':'form-input'})
        
        self.fields['content'].widget.attrs.update(
            {'class':'form-input-textarea'}
        )

        


