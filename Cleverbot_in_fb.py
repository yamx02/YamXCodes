#export PATH=$PATH:/home/yaminul/Downloads/geckodriver-v0.26.0-linux64  (set geckodriver in path)
from fbchat import Client
from fbchat.models import *
import time
import cleverbotfree.cbfree 
import sys
cb = cleverbotfree.cbfree.Cleverbot()
client=Client('yamin136635@gmail.com', 'yamin02')
client.isLoggedIn()
print(format(client.uid))
user = client.searchForUsers(input("With whom to chat:"))[0]
print("user's name: {}".format(user.name))
#messages = client.fetchThreadMessages(thread_id= '100007704161328', limit=1)
#for message in messages:
temp = 'it'
bot='it'
try:
    cb.browser.get(cb.url)
except:
    cb.browser.close()
    sys.exit()
while True:
	cb.get_form()
	messages = client.fetchThreadMessages(thread_id= user.uid, limit=1)
	for message in messages:
		p=message.text
	if temp==p or bot==p:			
		time.sleep(3)
		print("no reply")
	else:
		temp=message.text	
		cb.send_input(temp)
		bot = cb.get_response()
		print("she says: ",p)
		print("bot says: ",bot)
		client.send(Message(text=bot), thread_id=user.uid,thread_type=ThreadType.USER)
	time.sleep(5)
