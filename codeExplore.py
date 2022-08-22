#!C:\Users\lx\AppData\Local\Programs\Python\Python39\python.exe
import cgi
from googlesearch import search 

try:
    form = cgi.FieldStorage()
    searchTerm = form.getvalue('txtSearch')
except:
    print("Something went wrong")

print(searchTerm)


try:
    for result in search(searchTerm, tld="co.in",num=10,stop=10,pause=2):
        print(result)
except:
    print("something went wrong")


