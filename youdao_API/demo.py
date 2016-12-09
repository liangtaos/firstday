#/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import urllib2
import random
def getFanyi(q):
    appid = '20161209000033751'
    secretKey = 'jFatuMV_8cip3ULNB5CP'

    httpClient = None
    myurl = '/api/trans/vip/translate'
    fromLang = 'zh'
    toLang = 'auto'
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    url = 'api.fanyi.baidu.com'
    return 'http://'+url+myurl
    #try:
    #    httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
    #    httpClient.request('GET', myurl)
    #
    #    #response是HTTPResponse对象
    #    response = httpClient.getresponse()
    #    print response.read()
    #except Exception, e:
    #    print e
    #finally:
    #    if httpClient:
    #        httpClient.close()
url = getFanyi('大姚退役了，科比挂了，我依旧热爱篮球')
print url

print eval(urllib2.urlopen(url).read())['trans_result'][0]['dst']

