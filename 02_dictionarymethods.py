myDict = {
  "fast": "In a Quick Manner",
  "Harry": "A Coder",
  "Marks": [1,2,5],
  "anotherdict": {'harry':'player'},
  1:2
}

# Dictionary Methods
print(list(myDict.keys())) #Prints the keys of the dictionary
print (myDict.values()) #Prints the keys value of the Dicionary
print(myDict.items()) #Prints the (key,value) for the all contents of the dictionary
print(myDict)
updateDict = {
      "Lovish" : "Friend",
      'harry': 'A dancer',
      'Divya': 'Friend',
}
myDict.update(updateDict) # Update the dictionary by adding key value pairs from updateDict
print(myDict)

print(myDict.get("harry")) # Prints the value asssociated by adding key "harry"
print (myDict["harry"]) # Prints the value asssociated by adding key "harry"

# The difference between .get and [] syntax in Dictionaries
print(myDict.get("harry2")) # Returns None as harry2 is not present in the dictionary
print (myDict["harry2"]) # throws an error aas harry2 is not present in the dictionary

