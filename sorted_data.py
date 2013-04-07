from sys import argv
script, txt = argv

f = open(txt)
#can we read the file and take out the \n and : using a one line command?
captured_text = f.read().split("\n")
f.close()

#Earlier attempts in making tuples from list as: [('restaurant', number)] and so on...

#list1 = captured_text.split(":")
#["Arinell's", '4\nPancho Villa', '3\nAndalu', '3\nUrban Burger', '1\nEl Toro', '5']

#list_2 = captured_text.split("\n")
#["Arinell's:4", 'Pancho Villa:3', 'Andalu:3', 'Urban Burger:1', 'El Toro:5']
         
#create a dictionary where the keys are restaurant names and the values are scores for that restaurant.
dictionary = {}

for word in captured_text:
    clean_list = word.split(",")
    # ['Arinells', '4']
    # ['Pancho Villa', '3']
    # ['Andalu', '3']
    restaurant = clean_list[0]
    score = clean_list[1]
    dictionary[restaurant] = int(score)
	# alternate code = dictionary[temp_list[0]] = temp_list[1]

#first attempt at sorting the keys in alphabetical order
#tuples = dictionary.items()
#[('Urban Burger', 1), ('Little Baobab', 1), ('Casa Thai', 2)]
#sorted_list = sorted(tuples)
#[('Andalu', 3), ("Arinell's", 4), ('Bay Blend Coffee and Tea', 3)]

#what was actually used to sort the keys
#keys = dictionary.keys()
#sorted_keys = sorted(keys)
#combine the two above rows to get one line of code:
sorted_keys = sorted(dictionary.keys())
#['Andalu', "Arinell's", 'Bay Blend Coffee and Tea', 'Casa Thai']

#now retrieve the value of the key using ".get()"
for item in sorted_keys:
	score = dictionary.get(item)
	print "Restaurant %s is rated %s." % (item, score)



#previous attempts
#pseudocode example 1
# for i in new_dict:
# 	print "Restaurant %s is rated at %d." (new_dict.key(), new_dict.value()) 

#pseudocode example 2
#    i += 1         
#print "%s score is coming." % (index.restaurant[i])
     
#pseudocode example 3
#for restaurant in dictionary:
#    i += 1
#    print "%r is rated at %r." % (dictionary.keys(), dictionary.values())
    


