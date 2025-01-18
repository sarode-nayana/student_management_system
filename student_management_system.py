db = {101:{'name':'Nayana','marks':88,'roll':101,'fees':20000},     
     102:{'name':'Ram','marks':78,'roll':102,'fees':25000},    
     103:{'name':'Sham','marks':68,'roll':103,'fees':15000},    
     104:{'name':'Rina','marks':89,'roll':104,'fees':18000},
     105:{'name':'vaishu','marks':60,'roll':105,'fees':25000},    
     105:{'name':'komal','marks':70,'roll':106,'fees':20000}
     }
def dashboard():

    print('*'*60)
    print('\t\tWelcome To Student Management System for batch 459')
    print("""                    
                            Menu
                            1)Create Student Record
                            2)Read All Student
                            3)Update Student Record
                            4)Delete Student Record
                            5)Display student by fees paid status
                            6)Display student by marks status
    """)

def create_student():
   user_name = input('Enter Student Name:')
   user_roll = eval(input('Enter Student roll:'))
   user_marks = eval(input('Enter Student marks:'))
   user_fees = eval(input('Enter Student fees paid:'))
   
   chotu_dict = {}
   chotu_dict['name'] = user_name
   chotu_dict['marks'] = user_marks
   chotu_dict['roll'] = user_roll
   chotu_dict['fees'] = user_fees

   db[user_roll] = chotu_dict
   print(f"student {user_name} added successtully in db..........")
   print('*'*75)
   print()

def read_student():
    print('-'*65)
    print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r ='Roll number',n ='Name',m ='Marks',f ='fees'))
    print('-'*65)
    for i in db:
        print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r = db[i]['roll'],n = db[i]['name'],m = db[i]['marks'],f = db[i]['fees']))
        print('-'*65)


def update_student():
    user_roll = eval(input('Enter Student roll to update:'))
    if user_roll in db:
      user_name = input('Enter update Student Name:')
      user_marks = eval(input('Enter update Student marks:'))
      user_fees = eval(input('Enter update Student fees paid:'))
      db[user_roll]['name'] = user_name
      db[user_roll]['marks'] = user_marks
      db[user_roll]['fees'] = user_fees
      print(f"Student{db[user_roll]['name']} updated succesfully is db.....")
      print('-'*60)


def Delete_student():
    user_roll = eval(input('Enter Student roll to delete:'))
    if user_roll in db:
        n = db[user_roll]['name']
        del db[user_roll]
        print(f"Student {n} Delete Successfully from db......")
    else:
        print('Invalid student Roll no')


def read_student_fees():
    user_fees= eval(input('Enter student paid fees ammount to display :'))
    print('-'*65)
    print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r ='Roll number',n ='Name',m ='Marks',f ='fees'))
    print('-'*65)
    for i in db:
        if db[i]['fees'] >= user_fees:      # fees greater than equal uers fees logic
          print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r = db[i]['roll'],n = db[i]['name'],m = db[i]['marks'],f = db[i]['fees']))
          print('-'*65)

def read_student_marks():
    user_marks = eval(input('Enter student marks to display :'))
    print('-'*65)
    print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r ='Roll number',n ='Name',m ='Marks',f ='fees'))
    print('-'*65)
    for i in db:
        if db[i]['marks'] >= user_marks:     # marks greater than equal user marks logic
          print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r = db[i]['roll'],n = db[i]['name'],m = db[i]['marks'],f = db[i]['fees']))
          print('-'*65)

while True:
    dashboard()
    choice = eval(input('Enter Your Choice[1,2,3,4,5,6]:'))
    print('-'*70)

    if choice == 1:
        create_student()


    elif choice == 2:
        if len(db) == 0:
            print('No student to diplay in data base.....')
        else:
            read_student()


    elif choice == 3:
        if len(db) == 0:
            print('No student to update in data base.....')
        else:
           update_student()


    elif choice == 4:
        if len(db) == 0:
            print('No student to delete in data base.....')
        else:
           Delete_student()


    elif choice == 5:
        if len(db) == 0:
            print('No student to display in data base..... ')
        else:
            read_student_fees()

    elif choice == 6:
        if len(db) == 0:
            print('No student to display in data base....')
        else:
            read_student_marks()

    else:
        print('Invalid choice........')


    ch = input('Do You Want to Continue [Y/N]:')

    if ch.lower()!='y':
        break
