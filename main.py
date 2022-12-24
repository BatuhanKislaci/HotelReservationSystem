from txtStatements import saveTxt,loadTxt
from interface import Interface

customerList = []
roomList = []
totalRoomNumber = 3

def createRooms():
    for i in range(1,totalRoomNumber+1):
        roomList.append([i])

createRooms()

loadTxt(customerList,roomList)

myInterface = Interface(customerList,roomList,totalRoomNumber)
myInterface.showInterface()
customerList,roomList = myInterface.customerList,myInterface.roomList

saveTxt(customerList,roomList)