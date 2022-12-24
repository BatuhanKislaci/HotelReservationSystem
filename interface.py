from Hotel import Hotel

class Interface(Hotel):
  def __init__(self,customerList,roomList,totalRoomNumber):
    super().__init__(customerList,roomList,totalRoomNumber)

  def showInterface(self):
    ourProcess = input("What do you want to do?\nA) Make a reservation.\nB) Cancel my reservation.\nC) Extend my reservation.\nD) Check my reservation.\n")
    ourProcess.lower()
    customerName = input("What is your name?\n")
    if(ourProcess == "a"):
      self.answerA(customerName)
    elif(ourProcess == "b"):
      self.answerB(customerName)
    elif(ourProcess == "c"):
      self.answerC(customerName)
    elif(ourProcess == "d"):
      self.answerD(customerName)
    else:
      print(f"{customerName} please type only (a,b,c,d)!")
      self.showInterface()
    
  def loopInterface(self):
    question2 = input("Do you want to do anything else? Yes or No. \n")
    question2.lower()
    if(question2=="yes"):
      self.showInterface()
    else:
      print("Goodbye :)\n")

  def answerA(self,customerName):
    checkList = super().checkMyReservation(customerName)
    if len(checkList)==0:
        customersStartDate = input("When will your start your holiday? (dd.mm.yy)\n")
        howManyDays = int(input("How many days will you stay?\n"))
        freeRooms = super().checkFreeRooms(customersStartDate,howManyDays)
        if len(freeRooms)==0:
          print("Hotel is full for that dates!")
        else:
          super().addReservation(customerName,customersStartDate,howManyDays,freeRooms[0]) 
          print(f"Reservation added for {howManyDays} to room number {freeRooms[0]}") 
    else:
      print(f"You already have a reservation for {checkList[2]} days, started from {checkList[1]}") 
    
    self.loopInterface() 

  def answerB(self,customerName):
    checkList = super().checkMyReservation(customerName)
    if len(checkList)==0:
      print("You do not have a reservation")
    else:
      super().cancelMyReservation(checkList)
      print("Your reservation is cancelled")
    
    self.loopInterface() 

  def answerC(self,customerName):
    checkList = super().checkMyReservation(customerName)
    if len(checkList)==0:
      print("You do not have a reservation!")
    else:
      howManyDays = int(input("How many days will extend your reservation?\n"))
      if super().canExtendReservation(checkList,howManyDays):
        super().extendMyReservation(checkList,howManyDays)
        print("Your reservation extended!")
      else:
        print("Your room is not available for that days please make a new reservation for a different room")
    
    self.loopInterface() 
 
  def answerD(self,customerName):
    checkList = super().checkMyReservation(customerName)
    if len(checkList)>0:
      print(f"You have reservation for {checkList[2]} days started from {checkList[1]}. Your room number is : {checkList[3]}\n")
    else:
      print("You do not have a reservation")
    
    self.loopInterface() 



  
