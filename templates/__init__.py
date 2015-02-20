from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def final (tweets,searchTerm):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<!DOCTYPE html>\n'])
    extend_([u'<center>\n'])
    extend_([u'<title>Carla Results for ', escape_(searchTerm, True), u'</title>\n'])
    extend_([u'<div style="background-color:#ff6600;min-height:25px;width:85%;">\n'])
    extend_([u'</div>\n'])
    extend_([u'<h1 style="font-family:Verdana;">HN Birthday Countdown!</h1>\n'])
    extend_([u'<body style="font-family:Verdana;background-color:#f6f6ef;">\n'])
    for tweet in loop.setup(tweets):
        extend_([u'<p>', escape_(tweet, True), u'</p>\n'])
    extend_([u'</center>\n'])
    extend_([u'</body>\n'])

    return self

final = CompiledTemplate(final, 'templates/final.html')
join_ = final._join; escape_ = final._escape

# coding: utf-8
def oldregister(form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE html>\n'])
    extend_([u'<title>HN Birthday Countdown</title>\n'])
    extend_([u'<center>\n'])
    extend_([u'<div style="background-color:#ff6600;min-height:25px;width:85%;">\n'])
    extend_([u'</div>\n'])
    extend_([u'<h1 style="text-align:center;font-family:Verdana;">Unfortunately due to HN moving their API\n'])
    extend_([u'provider from thriftDB to algolia I will be dropping support for this site.\n'])
    extend_([u'<body></body><footer style="width:100%;height:28px;border-top:1px solid #000000;left:0px;text-align:center;position:absolute;bottom:0;font-size:8pt;">\n'])
    extend_([u'Made by dev1n on HN using the very cool <a href="https://www.hnsearch.com/api">HNSearch</a> API\n'])
    extend_([u'</footer>\n'])
    extend_([u'</center>\n'])

    return self

oldregister = CompiledTemplate(oldregister, 'templates/oldregister.html')
join_ = oldregister._join; escape_ = oldregister._escape

# coding: utf-8
def outputtest():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])

    return self

outputtest = CompiledTemplate(outputtest, 'templates/outputtest.csv')
join_ = outputtest._join; escape_ = outputtest._escape

# coding: utf-8
def register(form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!DOCTYPE html>\n'])
    extend_([u'<title>Carla Tweets</title>\n'])
    extend_([u'<center>\n'])
    extend_([u'<div style="background-color:#ff6600;min-height:25px;width:85%;">\n'])
    extend_([u'</div>\n'])
    extend_([u'<h1 style="font-family:Verdana;">Carla\'s Tweet Tracker!</h1>\n'])
    extend_([u'<body style="font-family:Verdana;background-color:#f6f6ef;">\n'])
    extend_([u'Enter a hashtag you wish to get tweets on and the app will begin <br>\n'])
    extend_([u'acquiring them.\n'])
    extend_([u'<form method="POST">\n'])
    extend_([u'    ', escape_(form.render(), False), u'\n'])
    extend_([u'</form>\n'])
    extend_([u'</body>\n'])
    extend_([u'</center>\n'])
    extend_([u'<center>\n'])
    extend_([u'<footer style="width:100%;height:28px;border-top:1px solid #000000;left:0px;text-align:center;position:absolute;bottom:0;font-size:8pt;">\n'])
    extend_([u'Made by dev1n on HN\n'])
    extend_([u'</footer>\n'])
    extend_([u'</center>\n'])

    return self

register = CompiledTemplate(register, 'templates/register.html')
join_ = register._join; escape_ = register._escape

