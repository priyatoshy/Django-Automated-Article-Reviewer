from multiprocessing import context
from turtle import title
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Article, Blog

# Create your views here.
def home(request):
    #return HttpResponse("<h2>Hospital Management System<h2>")
    #passing render and request
    #request is passed for later usage
    #we can also pass an data dicetionary
    if request.method=='POST':

        #getting the contents from the form

        article_title=request.POST['article_title']
        article_content=request.POST['article_content']

        #importing natural language procressing modules
        import spacy
        from  spacy.lang.en.stop_words import STOP_WORDS
        from string import punctuation
        from heapq import nlargest
        from textblob import TextBlob
        nlp=spacy.load('en_core_web_sm')
        text=article_content

        #creating stop words
        stopwords=list(STOP_WORDS)

        #loading the text into the nlp module
        doc=nlp(text)

        #computing the result
        #appending punctation
        punctuation+="\n"
        tokens=[token.text for token in doc]
        word_frequencies={}


        #creating a word frequecny table
        #def word_frequency_table_generator()
        for word in doc:
            if word.text.lower() not in stopwords:
                if word.text.lower() not in stopwords:
                     if word.text not in word_frequencies.keys():
                        word_frequencies[word.text]=1
                     else:
                        word_frequencies[word.text]+=1




        #normalizing frequency
        max_freqeuncy=max(word_frequencies.values())
        for word in word_frequencies.keys():
                word_frequencies[word]=word_frequencies[word]/max_freqeuncy

        #sentence tokenizations

        sentence_token=[sent for sent in doc.sents]



        #calculating sentence scores based on word score sum

        sentence_scores={}

        for sent in sentence_token:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent]=word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent]+=word_frequencies[word.text.lower()]



#creating a select length


        select_length=int(len(sentence_scores)*0.3)

        summary=nlargest(select_length,sentence_scores,key=sentence_scores.get)

        #converting to text

        final_summary=[word.text for word in summary]

        #joining into a text
        summary=' '.join(final_summary)

        summaryblob=TextBlob(summary)

        summarySentiment=summaryblob.sentiment
        
        summarySentiment=f"{summarySentiment}"


    

        context={'summary':summary,'sentiment':summarySentiment}

        if request.user.is_authenticated:
            username = request.user.username
            Article.objects.create(title=article_title,author=username,content=article_content,summary=summary,review=summarySentiment)
            return render(request,'home.html',context)
        
        else:
               
            return render(request,'home.html',context)
    


       
        
        


    
    else:
     
    
        return render(request,'home.html')


def blogs(request):
    blogs=Blog.objects.all()
    context={'blogs':blogs}
    return render(request,'blogs.html',context)


# Create your views here.
