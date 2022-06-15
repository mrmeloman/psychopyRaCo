import random
import os.path

#Create an empty-string variable
#for the conditions file name
condFileName = ""

#If there's a file storing files uses
if os.path.exists("assets/problems_randomisation.csv"):
    #Open the csv file
    randomization_file = open("assets/problems_randomisation.csv", "r")
    
    #Get a list of lines (separated by \n)
    lines = randomization_file.readlines()
    
    #Close the file
    randomization_file.close()
    
    #Create a dictionary (key:value collection)
    table = dict()
    
    #Create a sum variavle and initialize it with zero
    sum = 0
    
    #For every element in the list of lines
    for file_string in lines:
        #Get a list of substrings
        #using "," as separator
        items = file_string.split(",")
        #Store second element of this list
        #converted to int
        uses_int = int(items[1])
        #Add first element as string
        #and second element as int
        #To the dictionary
        table.update({items[0]:uses_int})
        
        #Add first element as int to a sum variable
        sum += uses_int
    
    #Store length of the dictionary
    #(ammount of key:value pairs)
    count = len(table)
    
    #Create an empty list for probabilities
    probs = []
    
    #For every key:value pair in the dictionary
    for uses in table.values():
        #Add this formula result
        #to the end of the probabilities list
        probs.append((1 - (uses/sum))*(1/(count - 1)))
    
    #Ignore commented code here and further on
    #print("probs:")
    #for p in probs:
    #    print(str(p))
    
    #Make a list of keys (file names)
    table_keys = list(table)
    
    #Choose the file name via weighted random
    #useing the probs list as weights list
    condFileName = random.choices(table_keys, weights = probs)[0]
    
    #Increment the number of uses
    table[condFileName] = table[condFileName] + 1
    
    #Clear the conditions file empty
    randomization_file = open("assets/problems_randomisation.csv","r+")
    randomization_file.truncate(0)
    randomization_file.close()
    
    #Create the empty string variable for new content
    new_content = ""
    
    #For every element of the dictionary
    for name in table:
        #Add key + comma + corresponding value + \n
        #to the new content variable
        new_content += name + "," + str(table[name]) + "\n"
    
    #Write new_content variable
    #to the conditions file
    randomization_file = open("assets/problems_randomisation.csv","w")
    randomization_file.writelines(new_content)
    randomization_file.close()
#If there's no randomisation file, 
#just choose by random
else:
    #The second number here should be
    #the ammount of your conditions files!
    fileIndex = random.randint(1, 4)
    #Also, they should be named "problems#"
    #where # is a number starting from 1
    condFileName = "conditions" + str(fileIndex) + ".csv"
