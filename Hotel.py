from Modules import date,extendedDate

class Hotel:
    def __init__(self,customerList,roomList,totalRoomNumber):
        self.customerList = customerList
        self.roomList = roomList
        self.totalRoomNumber = totalRoomNumber

    def checkFreeRooms(self,startDate,howManyDays):
        FreeRooms = []
        days = date(startDate,howManyDays)
        for i in self.roomList:
            FreeRooms.append(i[0])
            if len(i)==2:
                for j in i[1]:
                    if j in days:
                        FreeRooms.remove(i[0])
                        break   
        return FreeRooms


    def addReservation(self,customerName,startDate,howManyDays,customersRoom):
        self.customerList.append([customerName,startDate,howManyDays,customersRoom])
        days = date(startDate,howManyDays)   
        for d in days:
            if len(self.roomList[customersRoom-1])==1:
                self.roomList[customersRoom-1].append([d])
            else:
                self.roomList[customersRoom-1][1].append(d)

    
    def checkMyReservation(self,customersName):
        CheckList = []
        for i in self.customerList:
            if i[0] == customersName:
                CheckList = i
                break
        return CheckList

    
    def cancelMyReservation(self,checkList):
        self.customerList.remove(checkList)
        days = date(checkList[1],checkList[2])
        for d in days:
            self.roomList[checkList[3]-1][1].remove(d)


    def extendMyReservation(self,checkList,howManyDays):
        days = extendedDate(checkList[1],checkList[2],howManyDays)
        for i in self.customerList:
            if i == checkList:
                i[2] = i[2]+howManyDays
                break
        for d in days:
            self.roomList[checkList[3]-1][1].append(d)


    def canExtendReservation(self,checkList,howManyDays):
        isEmpty = True
        days = extendedDate(checkList[1],checkList[2],howManyDays)
        for d in self.roomList[checkList[3]-1][1]:
            if d in days:
                isEmpty = False
                break
        return isEmpty
        
        
         

    