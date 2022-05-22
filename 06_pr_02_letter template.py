letter = '''Dear <|NAME|>
            Greetings from abc coding house. I am happy to tell you about your selection
            you are selected!
            
            Date= <|DATE|>'''
name = input("Please enter your name\n")
date = input("PLease enter your date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print (letter)
