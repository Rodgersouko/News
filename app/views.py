from flask import render_template
from app import app
from newsapi import NewsApiClient




# Views

@app.route('/')
def index():
    newsapi= NewsApiClient('1123c65356c545bc97dfa6e49600d7fa')
    topheadlines = newsapi.get_top_headlines(sources='bbc-news,the-verge',)


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []


    for i in range(len(articles)):
        myarticles = articles[i]
        

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)


    return render_template('index.html', title = mylist)


@app.route('/news/<news_id>')
def news(news_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    title = f'You are viewing {news_id}'
    return render_template('news.html',title = title)
