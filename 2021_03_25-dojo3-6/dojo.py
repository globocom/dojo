def main():
    

    return True


def inputLength(inputList):
    return len(inputList) != 0

def countDown(inputList, k):
    if(not inputLength(inputList)): 
        return 0
        
    if(k not in inputList):
        return 0
    
    
    count = 0
    countGeral = 0
    for i in range(len(inputList)):
         if(inputList[i] == k and (i+k < len(inputList))):
             if(inputList[i+k] == 1):               
                 for j in range(k):
                     if(inputList[j] == k-1):
                        count = count + 1
                        if(count == k):
                            countGeral = countGeral + 1
    


    


    return countGeral
    
    # for i in range(len(inputList)):
    #     if(inputList[i] == k and (i+k < len(inputList))):
    #         if(inputList[i+k] == 1):
                
    #             for(j = k)

	
	# if(len(inputList) == 6):
    #     return 0
    # elif (k == 4):
    #     return 1
    # return 2