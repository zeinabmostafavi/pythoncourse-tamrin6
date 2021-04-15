import colorama
from colorama import Fore

# ------------------init--------------------

colorama.init()
print('Loading...')
# _ opening the databes file _
try:
    f = open('coursepython_tamrn6\product.csv')
except Exception as e:
    print("error: ", e)
    exit()
big_text = f.read()
parts = big_text.split('\n')
products = []
i = 0

# _ filling the product list in dictionary format _
while i < len(parts):
    info = parts[i].split(',')
    products.append({'ID': info[0], 'NAME': info[1],
                     'PRICE': info[2], 'COUNT': info[3]})
    i += 1
print(Fore.LIGHTCYAN_EX + 'data loaded! \nwelcome dear user!')

# -----------------process-------------------


def addNewProduct():
    print(Fore.LIGHTWHITE_EX +
          '_ adding a product _ \n**please enter the product details**')
    NAME = input('NAME: ')

    for i in range(len(products)):
        if NAME == products[i]['NAME']:
            print('this product exists in the store')
            break
    else:
        PRICE = input('PRICE: ')
        COUNT = input('COUNT: ')
        pID = int(products[len(products)-1]['ID']) + 1
        # _ update csv file _
        f = open('coursepython_tamrn6\product.csv', 'a')
        f.write('\n' + str(pID) + ',' + NAME +
                ',' + PRICE + ',' + COUNT)
        f.close()
        # _ update products list _
        products.append(
            {'ID': pID, 'NAME': NAME, 'PRICE': PRICE, 'COUNT': COUNT})

        print(Fore.GREEN + 'Done!')
    menu()


def search():
    user_input = input('enter ID or NAME of product: ')
    for product in products:
        if product['ID'] == user_input or product['NAME'] == user_input:
            print(product)
            break
    else:
        print('not found')

    menu()


def edit():

    user_edit = input("Enter id : ")
    for product in products:
        if product["ID"] == user_edit or product["NAME"] == user_edit:
            print("this is correct")
        u_product = input("Which Part To Edit? ")
        if u_product == "ID":
            ID = int(input("Enter New ID: "))
            product["ID"] = ID
            break
        elif u_product == "NAME":
            NAME = input("Enter New NAME: ")
            product["NAME"] = NAME
            break
        elif u_product == "PRICE":
            PRICE = input("Enter New PRICE: ")
            product["PRICE"] = PRICE
            break
        elif u_product == "COUNT":
            COUNT = input("Enter New COUNT: ")
            product["COUNT"] = COUNT
            break
    else:
        print("not found  this item")

    menu()


def remove():
    user_remove = input("Enter ID OR NAME : ")
    for product in products:
        if product["ID"] == user_remove or product["NAME"] == user_remove:
            print("please remove this item:")
            products.remove(product)
            print("removed")
            break
    else:
        print("not found")
    menu()


def buy():
    print("what product is need:")
    p_remove = input("Enter product: ")
    for product in products:
        if product["ID"] == p_remove or product["NAME"] == p_remove:
            print("this product is empty")
            p_count = input("Enter Number: ")
            if product["COUNT"] > p_count:
                result = int(product["COUNT"]) - int(p_count)
                print("rsolve it")
                break
            else:
                print("count is Not enough ")
                break
    else:
        print("count not found")
    menu()


def showAll():
    for i in range(len(products)):

        print('ID: ' + products[i]['ID'] + ',  NAME: ' + products[i]['NAME'] +
              ',  PRICE: ' + products[i]['PRICE'] + ',  COUUNT: ' + products[i]['COUNT'])
    menu()


def menu():
    print(Fore.LIGHTYELLOW_EX +
          '\n 1- add new product \n 2- search \n 3- edit \n 4- remove \n 5- buy \n 6- show all \n 7- exit')
    user_select = input('please enter the option you want: ')

    if user_select == '1':
        addNewProduct()
    elif user_select == '2':
        search()
    elif user_select == '3':
        edit()
    elif user_select == '4':
        remove()
    elif user_select == '5':
        buy()
    elif user_select == '6':
        showAll()
    else:
        exit()


menu()
