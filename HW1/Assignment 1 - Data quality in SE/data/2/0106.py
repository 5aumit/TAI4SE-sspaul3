# import datetime file from datetime module to use date and time functions
from datetime import datetime

# class created named as spy
class Spy:

    # constructor of Spy class.It is called automatically whenever the object of Spy class is created.
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

# class created named as ChatMessage
class ChatMessage:

    # constructor of ChatMessage class.It is called automatically whenever the object of ChatMessage class is created.
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


# instances of Spy class
# created default user for our spy
spy = Spy("Bhavikaa","Ms.",20,5.0)

#created default friends for our spy
friend_one = Spy("Sim","Ms.",21,4.8)
friend_two = Spy("Rupali","Ms.",20,4.0)
friend_three = Spy("James","Mr.",21,7.2)

friends = [friend_one,friend_two,friend_three]       #in friends list,we add these three default friends


