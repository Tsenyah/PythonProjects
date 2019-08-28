
heightBoolean = True
widthBoolean = True
plasterNotChosen = True
UndercoatNotChosen= True
paintNotChosen = True
hoursNotChosen = True

def multiply(width, height):
    return width * height

def display (area, paint, undercoat , plaster , cost ,hours ):
    total = cost + hours
    vat = 0.2 * total

    Gtotal = total + vat
    print("*********************"
          "\n Area Decorated : %8.2f "
          "\n Paint Used : %8.2f "
          "\n Plastering Applied ?:  %8.2f  " 
          "\n UnderCoat used?:  %8.2f " 
          "\n labour hours :  %8.2f "
          "\n VAT:  %8.2f " 
          "\n Grand Total :  %8.2f" % (area , paint ,plaster ,undercoat , hours , vat , Gtotal))



def pricePerSQM (area, paintCost, underCoatCost,platserCost,isWall ):
    if underCoat == 1:
        underCoatCost = 0.5

    if plastering == 1 and not isWall:
        plasterCost = 31
    elif plastering == 1 and isWall:
        plasterCost = 22.55

    return ((area*underCoatCost)+(area*plasterCost)+(area*paintCost))

def paintSelector():
    ok = True
    while ok:
        argument = int(input("Please Select which type of paint you would like\n"
                  "1)-Luxury quality which costs £3 per square metre\n"
                  "2)-Standard quality which cost £1.45 per square metre\n"
                  "3)-Economy quality which costs £0.75 per square metre \n"))
        switcher = {
            1: 3,
            2: 1.45,
            3: 0.75,
        }
        if argument == 1 or argument == 2 or argument == 3:
            ok = False
    return switcher.get(argument, "invalid choice")



print("Welcome to the estimation program")
while (heightBoolean):
    roomHeight = float(input("Please Enter the height of the wall\n"))
    if (roomHeight < 2.1 or roomHeight > 4.25):
        print("The height must be between 4.25m and 2.1m")
    else:
        heightBoolean = False
while(widthBoolean):
    roomWidth = float(input("Please enter the width of the room\n"))
    if(roomWidth <1.8 or roomWidth >7.5):
        print("The width must be between 1.8m and 7.5m")
    else:
        widthBoolean = False

while(plasterNotChosen):
    plastering = int(input("Would you like Plastering? £31psm for the celing and £22.50psm for the walls ?\n"
      "press '1' for yes or '0' for no \n"))
    if plastering == 0 or plastering ==1:
        plasterNotChosen = False
    else:
       print("invalid Selection please choose one or two")

paintPrice = paintSelector()

while(UndercoatNotChosen):
    underCoat = int(input("Would you like an UnderCoat? its an additional £0.50?\n"
      "press '1' for yes or '0' for no \n"))
    if underCoat == 0 or underCoat ==1:
        UndercoatNotChosen = False
    else:
       print("invalid Selection please choose one or two")

wallArea = 4 * multiply(roomWidth, roomHeight)
celingArea = multiply(roomWidth,roomWidth)
TotalArea = (pricePerSQM(wallArea,paintPrice,underCoat,plastering,True)
                +pricePerSQM(celingArea,paintPrice,underCoat,plastering,False))

while (hoursNotChosen):

        hoursworked = int(input("How many hours will this take to complete ?"))
        rate = hoursworked * 17.5
        if rate < 120:
            rate = 120

        hoursNotChosen = False


display((celingArea + wallArea), paintPrice, underCoat, plastering, TotalArea,rate)
