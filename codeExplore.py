print ("Content-type:text/html\r\n\r\n")
#!C:\Users\lx\AppData\Local\Programs\Python\Python39\python.exe
import cgi
from googlesearch import search
from furl import furl

try:
    form = cgi.FieldStorage()
    searchTerm = form.getvalue('txtSearch')
    fatchURL = furl(f"searchingProject/codeExplore.py/?txtSearch='{searchTerm}'") 
except:
    print("Something went wrong")

response = fatchURL.args['txtSearch']

print(searchTerm)


try:
    for result in search(response, tld="co.in",num=10,stop=10,pause=2):
        print(result)
except:
    print("something went wrong")

print(searchTerm)










