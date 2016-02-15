from obj import *

def shapeSortValue(shape):
    if type(shape) == Triangle:
        shapeType = 0
    elif type(shape) == Square:
        shapeType = 1
    elif type(shape) == Rectangle:
        shapeType = 2

    return shapeType

def colourSortValue(shape):
    if shape.colour == "green":
        colourType = 0
    elif shape.colour == "blue":
        colourType = 1
    elif shape.colour == "red":
        colourType = 2

    return colourType

def bubble(objList, sortVar, orderVar):
    swapCount = 0
    checkCount = 0
    # Shape order.
    #(triangle,square,rectangle) = (0,1,2)
    # Colour order.
    #(green,blue,red) = (0,1,2)
    
    for i in range(len(objList)):
        
        for item in objList:

            itemVal = shapeSortValue(item)
            colourVal = colourSortValue(item)
            itemIndex = objList.index(item)
            itemPrice = item.price
            checkCount += 1
            
            if sortVar == "shape":
                try:
                    if itemVal > shapeSortValue(objList[itemIndex+1]):
                        objList[itemIndex] = objList[itemIndex+1]
                        objList[itemIndex+1] = item
                        swapCount+=1
                    elif itemVal == shapeSortValue(objList[itemIndex+1]):
                        if itemPrice < objList[itemIndex+1].price:
                                objList[itemIndex] = objList[itemIndex+1]
                                objList[itemIndex+1] = item
                                swapCount+=1
                    else:
                        continue
        
                # When reached end of list.
                except:
                    print("Line complete")
                
            elif sortVar == "colour":
                try:
                    if colourVal > colourSortValue(objList[itemIndex+1]):
                        objList[itemIndex] = objList[itemIndex+1]
                        objList[itemIndex+1] = item
                        swapCount+=1
                    elif colourVal == colourSortValue(objList[itemIndex+1]):
                        if itemPrice < objList[itemIndex+1].price:
                            objList[itemIndex] = objList[itemIndex+1]
                            objList[itemIndex+1] = item
                            swapCount+=1
                    else:
                        continue
                
                # When reached end of list.
                except:
                    print("Line complete")
            
    #print("FINISHED")
    #print("Checks: " + str(checkCount) + " Swaps: " + str(swapCount))
    return objList

##rect2 = Rectangle(1,1,2,10,None,"blue")
##tri1 = Triangle(1,1,6,10,None,"green")
##sq1 = Square(1,1,3,10,None,"blue")
##rect1 = Rectangle(1,1,1,10,None,"green")
##tri2 = Triangle(1,1,5,10,None,"red")
##tri3 = Triangle(1,1,6.1,10,None,"green")
##
##objList = []
##objList.append(rect2)
##objList.append(sq1)
##objList.append(tri2)
##objList.append(rect1)
##objList.append(tri1)
##objList.append(tri3)
##
##for item in objList:
##    print(item)
##sortObjList = bubble(objList, "shape", "+")
##for item in sortObjList:
##    print(item)
##
##colourSortObjList = bubble(objList,"colour","-")
##for item in colourSortObjList:
##    print(item)
 
            
