name1=input("What is your name\n")
name2=input("What is your crush name\n")
combined_name=name1+name2
lower_name=combined_name.lower()
no_true=combined_name.count("t")+combined_name.count("r")+combined_name.count("u")+combined_name.count("e")
no_love=combined_name.count("l")+combined_name.count("o")+combined_name.count("v")+combined_name.count("e")
string_score=str(no_true)+str(no_love)
num_score=no_true+no_love
if num_score<10 or num_score>90:
    print(f"\nYour score is {string_score}, you go together like coke and mintos")
elif num_score>40 and num_score<50:
    print(f"\nYour score is {string_score}, you are alright together")
else:
    print(f"\nYour score is {string_score}")
