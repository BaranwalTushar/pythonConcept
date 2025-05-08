from  random import randint

class Train:

    def book(self,trainNo,fro,to):
        print(f"Ticket is booked Train No. is {trainNo} from {fro} to {to}")

    def getStatus(self,trainNo):
        print(f"Train No. this {trainNo} is running successfully")

    def getFare(self,trainNo,fro,to):
        print(f"Ticket fare in train no:{trainNo} from {fro} to {to} and fare is {randint(222,5000)}")


a = Train()
a.book(122311,"kolkata","Delhi")
a.getStatus(122311)
a.getFare(122311,'kolkata',"delhi")