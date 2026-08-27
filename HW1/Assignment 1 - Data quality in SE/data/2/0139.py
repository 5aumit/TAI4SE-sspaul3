# Duy B. Lam
# 61502602
# Project 3

# A module that reads the input and constructs the objects
# that will generate the program's output. This is the only
# module that should have an if __name__ == '__main__' block
# to make it executable; you would execute this module to run your program.


import Module1


#USED TO RETREIVE THE NUMBER OF LOCATIONS
def tripQuantity() -> int:
    try:
        locationQ = int(input())
        return locationQ
    finally:
        print('locationQ: ' + str(locationQ))

#USED TO RETREIVE THE NUMBER OF REQUESTED OUTPUTS        
def outputQ() -> int:
    try:
        outputQ = int(input())
        return outputQ
    finally:
        print('output quantity:' + str(outputQ))

#USED TO RECORD SEARCH LOCATIONS
def quantityToLocations(tripQ: int) -> list:
    locationCount = 0
    locationList = list()
    while (locationCount < tripQ):
        locationList.append(input())
        locationCount+=1
    return locationList    

#USED TO RECORD OUTPUT OPTIONS
def quantityToOutput(outputQ: int) -> list:
    outputCount = 0
    outputList = list()
    while (outputCount < outputQ):
        outputList.append(input())
        outputCount += 1
    return outputList


if __name__ == '__main__':
    
    #USED TO GET USER INPUTS
    locationQ = tripQuantity()
    locationList = quantityToLocations(locationQ) #print to double check
    
    #CREATES A NEW SEARCH INSTANCE AND IT'S REQUEST URL
    newSearch = Module1.URL()
    newSearch.set_from_location(locationList[0])
    newSearch.set_to_location(locationList[1:len(locationList)])
    print(str(newSearch.get_To_Location()))
    newSearch.set_request_url()
    newSearch_request_url = newSearch.get_Request_URL() #print to double check

    #THIS FUNCTION MAKES THE REQUEST AND GATHERS RESPONSE INTO DICTIONARY
    newSearch_reponse = newSearch.search_request_response()
    
    #USED TO GET USER OUTPUTS
    #outputQ = outputQ()
    #outputList = quantityToOutput(outputQ)
    #print(outputList)

   
    
    
    '''
    #USED TO REQUEST MAPQUEST SEARCH
    x = urllib.request.urlopen(url)
    
    #USED TO DECODE MAPQUEST RESPONSE
    y = x.read().decode(encoding = 'utf-8')
    print(y) # USE decoded response string to check with pretty json
    
    #USED TO CONVERT DECODED STRING TO DICT/LISTS
    z = json.loads(y) #dictionary of mapquest response which also includes lists

    print(type(z['route']['locations']))
    
    locationsList = z['route']['locations']
    print(locationsList)
    print(locationsList[1]['latLng'])
    i = 0
    if i < len(locationsList):
        for key in locationsList[i]:
            if key == 'latLng':
                print(locationsList[i][key])
                i+=1
####    i = 0
####    if i < len(locationsList):
####        if locationList[i] == 'latLng':
####            print(locationsList[i])
####        
    
    #print (y)
'''
