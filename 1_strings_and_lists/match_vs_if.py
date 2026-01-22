
# Employees and their offices
cairo = ['Islam Mahfouz', 'Mohamed Mesilhy',
         'Hatem Elmaghraby', 'Kareem Embaby']

riyadh = ['Mohamed Gouda', 'Ayman Hamed',
          'Seif Ali', 'Adham Wael']

casablanca = ['Ahmed Ashraf', 'Abd El-Rahman Mahrous',
              'Islam Sheta', 'Mohamed Medhat', 'Mahmoud Nasser']

dubai= ['Ahmed Alaa', 'Kareem Abd-Elmeged',
        'Osama Ashraf', 'Mohamed Mostafa', 'Ahmed Bedeir']

#get the name of offices
offices = input("Pleas enter the name of the offices : ").lower()

#print names of employees in that offices

match offices :
    case "cairo" | "egypt" | "eg" :
        name_offices = cairo
    case "riyadh" | "saudi srabia" | "ksa" :
        name_offices = riyadh
    case "casablanca" | "morocco" :
        name_offices = casablanca
    case "dubai" | "uae" :
        name_offices = dubai
    case _:
        name_offices = False
        print("Not found !")

if offices:
    print(f"The employees in {offices.upper()} are : {", ".join(name_offices[:-1])} and {name_offices[-1]}")
