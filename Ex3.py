# Create Kaun Banega Corepati KBC using Python

ques = ["What is the OS of this system?",
        "What is the full form of CWH?",
        "What's Your expected CTC in LPA?"]
options = [["A. Windows","B. Linux","C. Ubuntu","D. Mac OS"],
           ["A. cwh", "B. Code With Harry","C. Code with Harsh","D. Call with Harry"],
           ["A. 10","B. 20","C. 40","D. 60"]]
ans = ["A","B","D"]
price = [5000,10000,100000]
winning=0

print("Lets Begin the game")
print()
for i in range(0,len(ques)):
    print((i+1),". ",ques[i])
    print(options[i])
    print()
    ch = str(input("Select your option :- "))
    if(ch == ans[i]):
        print()
        print("Congrats!! You were right.")
        winning = winning + price[i]
        print("Your Total amount is ",winning)
        print()
    else:
        print()
        print("You Guessed it wrong")
        print()

print("Thank you!!")
print("You Won :- ",winning,"Rs")