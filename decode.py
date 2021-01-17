def firstLetterWord(str): 
  
    result = "" 
  
    # Traverse the string. 
    v = True
    for i in range(len(str)): 
          
        # If it is space, set v as true. 
        if (str[i] == ' '): 
            v = True
  
        # Else check if v is true or not. 
        # If true, copy character in output 
        # string and set v as false. 
        elif (str[i] != ' ' and v == True): 
            result += (str[i]) 
            v = False
  
    return result 
#Driver function


array = "India foxtrot. Yankee oscar uniform. Charlie alpha november. Uniform november delta echo romeo sierra tango alpha november delta.Tango hotel india sierra. Lima india kilo echo. Charlie oscar papa yankee. Alpha november delta.Papa alpha sierra tango echo.Tango oscar. Yankee oscar uniform romeo. Sierra tango alpha tango uniform sierra. - Lets see who gets it and follows the instructions. 🤔Where are my smart friends???"
print(firstLetterWord(array))