from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Article
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import ArticleForm
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
import re
import heapq
from summarizer import summarize
from engine.models import Article

      
#home function
class Home(View):
    
    def get(self,request):
        if request.user.is_authenticated:
            
    
            profile=request.user.profile
            if profile:#
                try:
                    articles=Article.objects.filter(writer=profile)
                except:
                    articles=[]
                if articles:
                    article=articles.first()

                    context={"data":profile,"article":article}
                else:
                    context={"data":profile,"article":None}
                
                return render(request,'engine/home.html',context)
            else:
                context={}
                return render(request,'engine/home.html',context)
        else:
            context={}
            return render(request,'engine/home.html',context)

        

    
class NewArticle(View):

    #@login_required
    def get(self,request):
        form=ArticleForm()
        context={"form":form}
        try:
            profile=request.user.profile
        except:
            profile=None
        if profile:
           
            articles=Article.objects.filter(writer=profile)
            print(articles)
        
            
            
            if articles:
                article=articles.first()
                context={"article":article,"form":form}
            else:
                context={"article":[],"form":form}
            
            return render(request,'engine/newblog.html',context)
        else:
            context={"article":[],"form":form}
            return render(request,'engine/newblog.html',context)
  
    #@login_required
    def post(self,request):
        if request.user.is_authneticated:
                form = ArticleForm(request.POST, request.FILES)
                if form.is_valid():
                    article=form.save(commit=False)
                    topic=request.POST["topic"]
                    content=request.POST["content"]
                    summaryblob=TextBlob(content)
                    summarySentiment=summaryblob.sentiment
                    polarity=summarySentiment.polarity
                    subjectivity=summarySentiment.subjectivity
                    sid_obj= SentimentIntensityAnalyzer()
                    emotion=sid_obj.polarity_scores(content)
                    negativity=emotion["neg"]
                    positivity=emotion["pos"]
                    neutrality=emotion["neu"]
                    compound_score=emotion["compound"]
                    # Input text - to summarize 
                    text=content
                    title=topic
                    summary = summarize(title, text)
                    summary = ' '.join(summary)
                    article.summary=summary
                    article.subjectivity=subjectivity
                    article.polarity=polarity
                    article.negativity=negativity
                    article.neutrality=neutrality
                    article.positivity=positivity
                    article.compound_score=compound_score
                    
                    try:
                        profile=request.user.profile
                        article.writer=profile
                    except:
                        profile=None
                    article.save()
                    if profile:
                        articles=Article.objects.filter(writer=profile)
                        
                        if articles:
                            article=articles.first()
                            context={"article":article,"form":form}
                        else:
                            context={"article":[],"form":form}
                        
                        return render(request,'engine/newblog.html',context)
                    else:
                        context={"article":[],"form":form}
                        return render(request,'engine/newblog.html',context)
       
        
                
            
            


 
#UPDATE SHOW AND DELETE OPERATIONS FOR EACH ARTICLE
        
    

class MyArticle(View):
    

    #show
    #@login_required
    def get(self,request,pk):
        article=Article.objects.get(id=pk)
        context={"data":article}
        #if article.writer==request.user:
        return render(request,"engine/single_project.html",context)


class AlterArticle(View):

    def get(self,request,pk):

        article=Article.objects.get(id=pk)
        form=ArticleForm(instance=article)
        return render(request,"engine/newblog.html",{'form':form})

    #update
    def post(self,request,pk):
                article=Article.objects.get(id=pk)
                form = ArticleForm(request.POST, request.FILES,instance=article)
                
                if form.is_valid():

                    
                    article=form.save(commit=False)
                    topic=request.POST["topic"]
                    content=request.POST["content"]
                    summaryblob=TextBlob(content)
                    summarySentiment=summaryblob.sentiment
                    polarity=summarySentiment.polarity
                    subjectivity=summarySentiment.subjectivity
                    sid_obj= SentimentIntensityAnalyzer()
                    emotion=sid_obj.polarity_scores(content)
                    negativity=emotion["neg"]
                    positivity=emotion["pos"]
                    neutrality=emotion["neu"]
                    compound_score=emotion["compound"]
                    # Input text - to summarize 
                    text=content
                    title=topic
                    summary = summarize(title, text)
                    summary = ' '.join(summary)
                    article.summary=summary
                    article.subjectivity=subjectivity
                    article.polarity=polarity
                    article.negativity=negativity
                    article.neutrality=neutrality
                    article.positivity=positivity
                    article.compound_score=compound_score
                    
                    try:
                        profile=request.user.profile
                        article.writer=profile
                    except:
                        profile=None
                    article.save()
                    return redirect ('/')
            
            
            
           
        #delete


class DeleteArticle(View):
    def get(self,request,pk):
        article=Article.objects.get(id=pk)
        if request.user==article.writer.user:
            return render(request,'engine/delete.html',{'obj':article})
        else:
            messages.error(request,"Invalid Request")
            return redirect("/")

    def post(self,request,pk):
        #=if the method is a post method
            if request.method=="POST":
                article=Article.objects.get(id=pk)
                article.delete()
                return redirect("/")

        
            #method1
     





