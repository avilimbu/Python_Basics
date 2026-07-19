# Can you change the self parameter inside a class to something else (say "rabbit"). 
# Try changing to 'slf' or "rabbit" and see the effect

#  Write a class Train which has methods to book a ticket,
#  get status(no of seats) and get fair information of a train.

from random import randint
class Train:

    def __init__(slf,TrainNo):
        slf.TrainNo = TrainNo

    def book(rabbit, fro, to):
        print(f"The trian no {rabbit.TrainNo} is booked form {fro} to {to}")
    def getstatus(self):
        print(f"the train no {self.TrainNo} is running in time")
    def getfair(self,fro,to):
        print(f"The ticket fair in train no {self.TrainNo} from {fro} to {to} is {randint(256,1500)}")

t = Train(12456)
t.book("Nepal", "India")
t.getstatus()
t.getfair("Nepal", "India")

# Yes we can change self parameter inside a class to something else.
# We use self to increase the readability of the code