def saveTxt(customerList,roomList):
  file = open("customerList.txt", "w")    
  for i in customerList:
    file.write(i[0] + "//" + i[1] + "//" + str(i[2]) + "//"+ str(i[3]) + "\n")   
  file.close()  

  file = open("roomList.txt","w")  
  for i in roomList:
    file.write(str(i[0]))
    for j in i[1]:
      file.write("//" + str(j)) 
    file.write("\n")  
  file.close() 

def loadTxt(customerList,roomList):
  file = open("customerList.txt", "r")
  for line in file:
    reservationDetails = line.strip().split("//")
    customerList.append([str(reservationDetails[0]),str(reservationDetails[1]),int(reservationDetails[2]),int(reservationDetails[3])])
  file.close()

  file = open("roomList.txt","r")
  x=0
  for line in file:
    reservationDetails = line.strip().split("//")
    newList = []
    for i in range(1,len(reservationDetails)):
      newList.append(str(reservationDetails[i]))
    roomList[x].append(newList)
    x=x+1
