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
    if shape.strColour == "green":
        colourType = 0
    elif shape.strColour == "blue":
        colourType = 1
    elif shape.strColour == "red":
        colourType = 2

    return colourType

def bubble(objList, sortVar, orderVar):
    swapCount = 0
    checkCount = 0
    
    for i in range(len(objList)):
        
        for item in objList:

            itemVal = shapeSortValue(item)
            colourVal = colourSortValue(item)
            itemIndex = objList.index(item)
            itemPrice = item.price
            checkCount += 1

            if orderVar == "Ascending":
                if sortVar == "Shape":
                    try:
                        if itemVal > self.shapeSortValue(objList[itemIndex+1]):
                            objList[itemIndex] = objList[itemIndex+1]
                            objList[itemIndex+1] = item
                            swapCount+=1
                        elif itemVal == self.shapeSortValue(objList[itemIndex+1]):
                            if itemPrice < objList[itemIndex+1].price:
                                objList[itemIndex] = objList[itemIndex+1]
                                objList[itemIndex+1] = item
                                swapCount+=1
                        else:
                            continue
        
                # When reached end of list.
                    except:
                        pass
                        #print("Line complete")
                
                elif sortVar == "Colour":
                    try:
                        if colourVal > self.colourSortValue(objList[itemIndex+1]):
                            objList[itemIndex] = objList[itemIndex+1]
                            objList[itemIndex+1] = item
                            swapCount+=1
                        elif colourVal == self.colourSortValue(objList[itemIndex+1]):
                            if itemPrice < objList[itemIndex+1].price:
                                objList[itemIndex] = objList[itemIndex+1]
                                objList[itemIndex+1] = item
                                swapCount+=1
                        else:
                            continue
                
                    # When reached end of list.
                    except:
                        pass
                        #print("Line complete")
                else:
                    raise ValueError("sortVar must be either \"Colour\" or \"Shape\"")

            elif orderVar == "Descending":
                if sortVar == "Shape":
                    try:
                        if itemVal < shapeSortValue(objList[itemIndex+1]):
                            objList[itemIndex] = objList[itemIndex+1]
                            objList[itemIndex+1] = item
                            swapCount+=1
                        elif itemVal == shapeSortValue(objList[itemIndex+1]):
                            if itemPrice > objList[itemIndex+1].price:
                                    objList[itemIndex] = objList[itemIndex+1]
                                    objList[itemIndex+1] = item
                                    swapCount+=1
                        else:
                            continue
            
                    # When reached end of list.
                    except:
                        pass
                        #print("Line complete")
                    
                elif sortVar == "Colour":
                    try:
                        if colourVal < colourSortValue(objList[itemIndex+1]):
                            objList[itemIndex] = objList[itemIndex+1]
                            objList[itemIndex+1] = item
                            swapCount+=1
                        elif colourVal == colourSortValue(objList[itemIndex+1]):
                            if itemPrice > objList[itemIndex+1].price:
                                objList[itemIndex] = objList[itemIndex+1]
                                objList[itemIndex+1] = item
                                swapCount+=1
                        else:
                            continue
                    
                    # When reached end of list.
                    except:
                        pass
                                     
                else:
                    raise ValueError("sortVar must be either \"Colour\" or \"Shape\"")
            else:
                raise ValueError("orderVar must be either \"Descending\" or \"Ascending\"")
    #print("FINISHED")
    #print("Checks: " + str(checkCount) + " Swaps: " + str(swapCount))
    return objList

            
