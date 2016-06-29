import urllib
import re



htmltext = urllib.urlopen("http://www.leboncoin.fr/annonces/offres/ile_de_france/?th=1&q=xiaomi").read()
regex = '<h3 class="item_price">(.+?)</h3>'

pattern = re.compile(regex)


result  = re.findall(pattern, htmltext)

print "print le resultat. \n"
print result
myresult = [i.split('&nbsp;&euro')[0] for i in result]

print "print my resultat. \n"
print myresult

print 'hhlo'

