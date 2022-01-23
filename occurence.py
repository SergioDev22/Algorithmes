def count_substring(string, sub_string):
    text = []
    sub_text = []
    count = 0
    for i in range(len(string)):
        text.append(string[i])
    for y in range(len(sub_string)):
    	sub_text.append(sub_string[y])

    index = []
    for index,item in enumerate(text):
    	if item == sub_text[0]:
        	sub_string_in_string = "".join(text[index:index+len(sub_text)])
        	if sub_string_in_string == sub_string:
        		count = count + 1
        	pass

    return count

if __name__ == '__main__':
    string = input("Entrer la chaine: ").strip()
    sub_string = input("Entrer le mot à chercher dans la chaine: ").strip()
    
    count = count_substring(string, sub_string)
    print(f"L'occurence de ce mot à chercher vaut {count} dans cette chaine")
