
from email.headerregistry import Address
import imp

from utils import *



con = create_connection()
create_table(con)

while True:

    print("---------------------------------Menu---------------------------------")
    print("For Insert  [1]")
    print("For Select  [2]")
    print("For Update  [3]")
    print("For Delete  [4]")

    keys = int(input(" Choice: "))

    if keys ==1:
        sel = select(con)
        next_id = sel[-1][0] + 1

        name = input("Name: ")
        surname = input("Surname: ")
        age = input("Age: ")
        address = input("Address: ")
        position = input("Position: ")

        infos = (next_id, name, surname, age, address, position, 1)
        insert(con, infos)

    elif keys == 2:
        data = select(con)
        for rows in data:
            print(rows)

    elif keys ==3:
        data = select(con)
        for rows in data:
            print(rows)

        sel_by_id = int(input("Updated id: "))

        row = select_by_Id(con, sel_by_id)
        print(row)


        info = list(row[0])

        action = int(input("Ad deyisdirilsin mi? [1/0]"))
        if action ==1:
            name= input("Yeni ad: ")
            info[1]= name


        action = int(input("Soyad deyisdirilsin mi? [1/0]"))
        if action ==1:
            surname= input("Yeni soyad: ")
            info[2]= surname


        action = int(input("Yas deyisdirilsin mi? [1/0]"))
        if action ==1:
            age= input("Yeni yas: ")
            info[3]= age


        action = int(input("Unvan deyisdirilsin mi? [1/0]"))
        if action ==1:
            address= input("Yeni unvan: ")
            info[4]= address


        action = int(input("Vezife deyisdirilsin mi? [1/0]"))
        if action ==1:
            position= input("Yeni vezife: ")
            info[5]= position


        print(info)
        entity = info[1:]
        entity.append(info[0])
        update(con, tuple(entity))

    elif keys ==4:
        data = select(con)
        for rows in data:
            print(rows)
        del_id = int(input("Deleted id: "))
        delete(con, del_id)




