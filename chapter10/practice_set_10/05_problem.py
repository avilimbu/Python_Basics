#  Write a class Train which has methods to book a ticket,
#  get status(no of seats) and get fair information of a train.

from random import randint
class Train:

    def __init__(self,TrainNo):
        self.TrainNo = TrainNo

    def book(self, fro, to):
        print(f"The trian no {self.TrainNo} is booked form {fro} to {to}")
    def getstatus(self):
        print(f"the train no {self.TrainNo} is running in time")
    def getfair(self,fro,to):
        print(f"The ticket fair in train no {self.TrainNo} from {fro} to {to} is {randint(256,1500)}")

t = Train(12456)
t.book("Nepal", "India")
t.getstatus()
t.getfair("Nepal", "India")