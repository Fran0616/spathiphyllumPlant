Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #this program will take a string and check to see if it matches the word Spathiphyllum
#if it does it will print "Yes Spathiphyllum is the best plant ever!""
#if the word Spathiphyllum is lowercase it will print "No I want a big Spathiphyllum!"
#if you input anything else it will print out ""Spathiphyllum! Not [input]!""
plant = input("Enter the word Spathiphyllum: ")

if plant == "Spathiphyllum":
    print ("Yes " + plant + "is the best plant ever!")


elif plant == "spathiphyllum":
    print("No I want a big Spathiphyllum!")
    
    
else:
    print("Spathiphyllum! Not " + plant + "!")
