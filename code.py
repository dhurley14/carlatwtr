import web
import urllib2
import json
urls = (
    "/.*","hello"
)

app = web.application(urls,globals())

class hello:
    def GET(self):
        mylist = []
        url = urllib2.urlopen("https://api.thriftdb.com/api.hnsearch.com/users/"+
        "_search?q=api&pretty_print=true")
        content = url.read()
        jdata = json.loads(content)
        print 'choices: \n',jdata.keys()
        #print jdata['results'][0]['item']
        for i in range(len(jdata['results'])):
            for key,value in jdata['results'][i]['item'].iteritems():
                if('karma' in key):
                    return str(jdata['results'][i]['item']['username']) + " " + str(key) + " " +str(value)

        #return 'Hello Devin!!'

app = app.gaerun()
