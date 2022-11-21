#!/usr/bin/python3

import requests
import webbrowser

chrome_path = '/usr/bin/google-chrome %s'

session = requests.Session()

url="http://demo.testfire.net/login.jsp"

data= {
	
"uid":"admin",
"passw":"admin",
"btnSubmit":"Login"


}


session.post(url,data=data)

cont = session.get("http://demo.testfire.net/bank/main.jsp")

file = open('website.html','wb')  # contents are encoded ,here using b to write as encoded
file.write(cont.content)
file.close()
webbrowser.get(chrome_path).open("website.html")


