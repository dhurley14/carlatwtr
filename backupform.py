import web
import urllib2
import json
from datetime import datetime
import time
from web import form
import sys
sys.path.insert(0,'lib')
from twython import Twython
import logging
import StringIO

urls = ('/.*','register',
        '/download', 'download'
        )
app = web.application(urls,globals())
render = web.template.render('templates/') 

register_form = form.Form(
    form.Textbox("hashtag", description="Hashtag:"),
    form.Button("Get tweets!",type="button",description="Get tweets containing this hashtag"),
    validators = []
)
"""
class download:

    def GET(self):
        web.
"""
class register:
    def GET(self):
        #do $:f.render() in the template
        f = register_form()
        return render.register(f)

    def get_tweets(self, search_term, **kwargs):
        """ Get a user's timeline

        :param username: (default pmarca)
        :param tweetID: 
        """
        twitter = self.get_authentication()

        # to get all 3200 possible tweets, I must cycle
        # through, and change the max_id on each call to be the lowest
        # id , so that my next call gets all the tweets below that id,
        # and so on and so forth.
        user_timeline = ""

        if len(kwargs) == 0:
            user_timeline = twitter.search(q=search_term, count=100)
        else:
            user_timeline = twitter.search(q=search_term, count=100, max_id=kwargs['anId'])    

        return user_timeline


    def POST(self):

        try:
            #twitter = self.get_authentication()
            #user_timeline = twitter.get_user_timeline(screen_name=web.input().hashtag, count=200)
            searchTerm = web.input().hashtag
            logging.info(searchTerm)
            searches = self.get_tweets(searchTerm)#twitter.search(q=web.input().hashtag, count=200)
            logging.info("size of searches: "+str(len(searches['statuses'])))
            logging.info("ID ---> "+str(searches['statuses'][len(searches['statuses'])-1]['id']))
            tweets = [item['text'] for item in searches['statuses']]
            old_max_id = 0
            new_max_id = 1
            someIndex = 0
            for i in xrange(3):
                old_max_id = searches['statuses'][len(searches['statuses'])-1]['id']
                searches = self.get_tweets(searchTerm, anId=old_max_id)
                #new_max_id = searches['statuses'][len(searches['statuses'])-1]['id']

                logging.info("old_max_id ----------------> "+str(old_max_id))
                #logging.info("new_max_id ================> "+str(new_max_id))
                logging.info("\nCREATED AT DATE -------------> "+str(searches['statuses'][len(searches['statuses'])-1]['created_at']))
                logging.info("size of searches after max_id: "+str(len(searches['statuses'])))

                for item in searches['statuses']:
                    tweets.append(item['text'])

                #twits.append([item['text'] for item in searches['statuses']])
                #logging.info("size of twits: "+str(len(twits)))
                someIndex += 1

            #tweets = len(twits)
            
        except Exception, e:
            logging.exception(e)


        try:
            output = StringIO.StringIO()
            for tweet in tweets:
                output.write(str(tweet.encode('utf-8'))+'\n')
            doc = output.getvalue()
            output.close()
            app.response.header("Content-Disposition", "attachment; filename=hello.csv")
            app.response.out.write(doc)
        except Exception, e:
            logging.exception(e)
        #web.header("Content-Type", 'csv')

        """
        self.response.headers['Content-Type'] = 'text/csv'
        self.response.out.write(','.join(['a', 'cool', 'test']))
        self.response.headers['Content-Disposition'] = "attachment; filename=fname.csv"
        """
        #for item in searches['statuses']:
        #    tweets.append(item['text'])
        #greeting = str(user_timeline[0]['text'])
        #greeting2 = str(user_timeline[1]['text'])
        #greeting = web.input().hashtag
        #greeting2 = " that was the greeting "
        # calculate birthday
        """url = urllib2.urlopen("https://api.thriftdb.com/api.hnsearch.com/users/_search?q="+web.input().username+"&pretty_print=true")
        jdata = json.loads(url.read())
        joinDate = jdata['results'][0]['item']['create_ts']
        
        year = joinDate[:4]
        month = joinDate[5:7]
        day = joinDate[8:10]
        """
        #currentY = datetime.today().year
        #currentM = datetime.today().month
        #currentD = datetime.today().day
        """
        
        d=datetime(int(joinDate[:4]),int(joinDate[5:7]),int(joinDate[8:10]),0,0,0)
        
        if(int(joinDate[5:7]) <= int(datetime.today().month)):
            newD = datetime(int(datetime.today().year)+1, int(joinDate[5:7]),int(joinDate[8:10]),0,0,0)
        else:
            newD = datetime(int(datetime.today().year),int(joinDate[5:7]),int(joinDate[8:10]),0,0,0)
        
        dTime = (newD-datetime.today()).days
        greeting = str(jdata['results'][0]['item']['username'])+ " joined HN on " +day+'/'+month+'/'+year

        greeting2 = str(jdata['results'][0]['item']['username'])+ " " + str('has') + " " + str(dTime) + " days left until their next HN Birthday!"
        """
        return render.final(tweets,searchTerm)#greeting,greeting2)

        #return web.input().username"""


    def get_authentication(self):
        """ Get a connection to the Twitter API using Twython.

        return a new instance of the Twython object.
        """
        APP_KEY = 'iD0lOpbSKZ35Fs6CjKxisPuKn'
        APP_SECRET = 'n4bqzvLa0dim6U03OM5dDAeTlSjRqi9sZ7YkNY6FBgSyv6JvtV'
        twitter = Twython(APP_KEY, APP_SECRET)
        return twitter
        
app = app.gaerun()

