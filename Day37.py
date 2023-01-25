# Today After the exam we will be learning more about finnaly keyword tyhat comes under the topic of exception handling

'''
What is the use of Finally keyword?
=> It is always Executed
'''

def func():
    try:
        l = [1,2,3,4,5]
        i = int(input("Enter index :- "))
        print(l[i])
        return l[i]
    except Exception as e:
        print("Some error Occurrred!!!")
        print("Error :- ",e)
        return 0
    finally:
        print("Don't Worry I am always executed")

x = func()

print("Function Executed with error code : ",x)