class person:
    def __init__(self,name,number):
        self.name = name
        self.numbers = []
        self.numbers.append(number)

def search(list):
    for people in list:
        if people.name==name:
            return people
    else:
        return None

def display(list):
    print('Name  |  NUMBERS ')
    print('-----------------')
    for people in list:
        print(people.name,': ',people.numbers)

def search_key(list,key):
    print('\n')
    keyword_names = []
    for people in list:
        if key in people.name:
            keyword_names.append(people)
    if not keyword_names:
        print("      *no person found with this keyword.")
    else:
        print("Founded names are as given below,")
        id=0;
        for people in keyword_names:
            print('   ',id+1,':',people.name)
            id+=1
        print('\n')
        nb = int(input("Enter person's id(which is written before name) to get his(her) numbers :"))
        print('\n',keyword_names[nb-1].name,':',keyword_names[nb-1].numbers)

if __name__=='__main__':
    list = []
    exit = False
    time = 1
    while not exit:
        print('\n')
        task = int(input('Enter 1(store contact) or 2(search contact) or 3(print contacts) or 4(exit) : '))
        if task==1:
            print('\n')
            name = input("Enter Name : ")
            while(True):
                MB = input("Mobile Number : ")
                if(len(MB)==10):
                    try:
                        MB = int(MB)
                        break
                    except ValueError:
                        print("      Not a number! try again.")
                else:
                    print("     *please enter valid number")
            MB = int(MB)
            found = search(list)
            if found:
                found.numbers.append(MB)
            else:
                list.append(person(name,MB))
            list = sorted(list, key=lambda item: item.name.casefold())
        elif task==2:
            print('\n')
            key = input("Enter keyword :")
            search_key(list,key)
        elif task==3:
            print('\n')
            if(list):
                display(list)
            else:
                print("      *ContactKeeper is empty")
        else:
            exit = True