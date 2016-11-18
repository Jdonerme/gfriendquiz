from app import app

from flask import render_template, flash, redirect, session
from app import app
from .forms import *
import random as rand
import spotipy


class GFriend:
    SOWON = 0
    YERIN = 1
    EUNHA = 2
    YUJU = 3
    SINB = 4
    UMJI = 5    
    gfriend = ['Sowon', 'Yerin', 'Eunha', 'Yuju', 'SinB', 'Umji']

    sowonBio = "You and Sowon would be a perfect match. You both take care of others " \
                "around you and would be cute looking after each other."
    yerinBio = "You and Yerin go toegther like white on rice. You two would get " \
                "into all kinds of fun shenanigans together."
    eunhaBio = "You and Eunha make a cute pair. Both of you are adorable and sweet." \

    yujuBio = "Yuu and Yuju are meant to be. Both of you are talented and fun."
    sinBBio = "You and SinB should be a hot new couple. Both of you just want " \
                "to have fun, laugh out loud, and dance the night away."
    UmjiBio = "You and Umji would be great together. Your sweetheart nature is" \
        " a perfect complement to Umji's cuteness." 


    bios = {'Sowon': sowonBio,
            'Yerin': yerinBio, 
            'Eunha': eunhaBio, 
            'Yuju': yujuBio,
            'SinB': sinBBio, 
            'Umji': UmjiBio}
    uri = 'spotify:artist:0qlWcS66ohOIi0M8JZwPft'
class Constants:
    OFFBYONE = 1.0 / 3
    ALMOST = 0.5


def prep(l):
    result = []
    for i in range(len(l)):
        result.append((i, l[i]))
    return result


def givePoints(key, results, i):
    results[key[i]] += 1
    
    if(i == 0):
        results[key[i+1]] += Constants.ALMOST
    elif(i == 5):
       results[key[i-1]] += Constants.ALMOST
    else:
       results[key[i-1]] += Constants.OFFBYONE
       results[key[i+1]] += Constants.OFFBYONE    
    return 1

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
                           title='Sign In',
                           form=form)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    form = IndexForm()
    if(form.is_submitted()):
        return redirect('/one')
        
    return render_template('index.html', form = form)

@app.route('/one', methods = ['GET', 'POST'])
def QuestionUno():
    form = Question()
    form.response.choices =  [(0, "Not at all"), (1, 'no'), (2, 'meh'), (3, 'kind of'), (4, "I'm p decent"), (5, 'Hella')]
    question = 'How well can you sing?'
    results = [0.0] * 6
    if(form.is_submitted()):
        try:
            i = int(form.response.data) 

            rankingKey = [GFriend.SOWON, GFriend.UMJI, GFriend.YERIN, GFriend.SINB, GFriend.EUNHA, GFriend.YUJU]
            givePoints(rankingKey, results, i)
            session['results'] = results
            return redirect('/two')
        except(ValueError):
            render_template('Question.html', 
                               question= question,
                               form=form)
        return redirect('one')
        
    return render_template('Question.html', 
                           question = question, img = 'one.jpg',
                           form = form)

@app.route('/two', methods = ['GET', 'POST'])
def QuestionDos():
    form  = Question()
    question = 'How well can you dance?'
    form.response.choices = [(0,"I can't even walk straight"), (1,'What is this "dance?"'), (2,'ehhhhhh'), (3,"I'm ok"), (4,'like a mo fo'), (5,'I invented dancing')]
    results = session['results']
   
    if(form.is_submitted()):
        try:
            i = int(form.response.data)
            rankingKey = [GFriend.SOWON, GFriend.EUNHA, GFriend.UMJI, \
                  GFriend.YUJU, GFriend.YERIN, GFriend.SINB]
            givePoints(rankingKey, results, i)
            session['results'] = results
            return redirect('/three')       
        except(ValueError):
            return redirect('/two')  
  
    return render_template('Question.html', 
                           question= question, img = 'two.jpg',
                           form=form)

@app.route('/three', methods = ['GET', 'POST'])
def QuestionTres():
    form  = Question()
    question = 'Are you a visual?'
    form.response.choices = prep(["U - G - L Y, I don't have an alibi", "My mom thinks I'm cute", "I'm ok I guess", '*winks*', "My looks are killer", "I'm a Greek Deity"])
    results = session['results']
    if(form.is_submitted()):
        try:
            i = int(form.response.data)
            rankingKey = [GFriend.UMJI, GFriend.YUJU, GFriend.EUNHA, \
                  GFriend.SINB, GFriend.YERIN, GFriend.SOWON]
            givePoints(rankingKey, results, i)   
            return redirect('/four')
        except(ValueError):
            render_template('Question.html', 
                            question= question, one = True,
                            form=form)  
            session['results'] = results
            return redirect('/three')

    
    return render_template('Question.html', 
                           question= question, img = 'three.jpg',
                           form=form)
@app.route('/four', methods = ['GET', 'POST'])
def QuestionQuatro():
    form  = Question()
    question = 'Are you a cutie pie?'
    form.response.choices =  prep(["Rachael wouldn't call me cute", "yeah, that's a no", 'maybe a cutie potato', 'i is a qt', "das me, I'm cute", "Cuter than Joon's smile"])
    results = session['results']
    if(form.is_submitted()):
        try:
            i = int(form.response.data)
            rankingKey =  [GFriend.YUJU, GFriend.SOWON, GFriend.SINB, \
                  GFriend.YERIN, GFriend.EUNHA, GFriend.UMJI]
            givePoints(rankingKey, results, i)
            session['results'] = results
            return redirect('/five')
        except(ValueError):
            return redirect('/four')

    
    return render_template('Question.html', 
                           question= question, img = 'four.jpg',
                           form=form)
@app.route('/five', methods = ['GET', 'POST'])
def QuestionCinco():
    form  = Question()
    question = 'Do you have a 4D personality?'
    form.response.choices = prep(["I watch paint dry for fun", 'Quirky bad', "I'm simple folk", 'Quirky good', \
                                "I was on running man", "I'm N dimensional! (n >> 4)"])
    results = session['results']
    if(form.is_submitted()):
        try:
            i = int(form.response.data)
            rankingKey =  [GFriend.EUNHA, GFriend.UMJI, GFriend.SOWON, \
                    GFriend.SINB, GFriend.YUJU, GFriend.YERIN]  
            givePoints(rankingKey, results, i)
            session['results'] = results 
            return redirect('/six')
        except(ValueError):
            return redirect('/five')
    return render_template('Question.html', 
                           question=question, img = 'five.jpg',
                           form=form)
@app.route('/six', methods = ['GET', 'POST'])
def QuestionSix():
    question = "Are you mature?"
    form  = Question()
    form.response.choices = prep(["THAT'S WHAT SHE SAID", 'Hmmm. No no', 'I like to whine a lot', "I'm growing up", "people always think I'm older than I am",\
                                "I'm the parent in my friend group"])
    results = session['results']
    if(form.is_submitted()):
        try:
            i = int(form.response.data)
            rankingKey =  [GFriend.YERIN, GFriend.UMJI, GFriend.SINB, \
              GFriend.YUJU, GFriend.EUNHA, GFriend.SOWON]
            givePoints(rankingKey, results, i)
            session['results'] = results
            return redirect('/seven')
        except(ValueError):
            return redirect('/six')
    return render_template('Question.html',  
                           question='Are you mature?', img = 'six.jpg',
                           form=form)
@app.route('/seven', methods = ['GET', 'POST'])
def QuestionNueva():
    results = session['results']
    form  = Question()
    question = 'Does Joe Donermeyer Love you?'
    form.response.choices = prep(["Who is that?", "We don't get along", 'Unclear EOM', "We're good friends", \
        "We're BFFLs", 'More than anything'])
    if(form.is_submitted()):
        try:
            i = int(form.response.data)
            rankingKey =  [GFriend.SOWON, GFriend.YERIN, GFriend.UMJI, \
                  GFriend.YUJU, GFriend.SINB, GFriend.EUNHA]    
            givePoints(rankingKey, results, i)
            session['results'] = results 
            return redirect('/result')
        except(ValueError):
            return redirect('/seven')
    session['results'] = results
    return render_template('Question.html', 
                           question= question, img = 'seven.jpg',
                           form=form)

@app.route('/result', methods = ['GET', 'POST'])
def final():
    form = Result()
    results = session['results']
    #results = [0] * 6
    point = max(results)
    final = []
    for i in range(len(GFriend.gfriend)):
        if(results[i] == point):
            final.append(GFriend.gfriend[i])
    match = rand.choice(final)
    bio = GFriend.bios[match]

    gfriend_uri = GFriend.uri

    spotify = spotipy.Spotify()
    songs = spotify.artist_top_tracks(gfriend_uri)
    uri_str = ''

    for track in songs['tracks']:
        uri_str += track['uri'][14:]
        uri_str += ','
   
    if(form.is_submitted()):
        session['results'] = [0] * 6
        return redirect('/index')
    
    img = match + ".gif"
 
    return render_template('final.html', match = match, img = img,
                       bio = bio, form = form, uris = uri_str)
