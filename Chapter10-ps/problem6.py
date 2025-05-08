from  random import randint

class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(HARRY,fro,to):
        print(f"Ticket is booked Train No. is {HARRY.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train No. this {self.trainNo} is running successfully")

    def getFare(self,fro,to):
        print(f"Ticket fare in train no:{self.trainNo} from {fro} to {to} and fare is {randint(222,5000)}")


a = Train(1222)
a.book("kolkata","Delhi")
a.getStatus()
a.getFare('kolkata',"delhi")