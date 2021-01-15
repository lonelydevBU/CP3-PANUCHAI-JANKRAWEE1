product = {101:["สบู่",24.50],102:["ผงซักฟอก",27.50],\
           103:["น้ำดื่ม",8.50],104:["แปรงสีฟัน",35.00],\
           105:["ยาสีฟัน",60.75],106:["แป้งเด็ก",32.50],\
           107:["บะหมี่",6.25],108:["ข้าวสาร",185.00],\
           109:["น้ำมันพืช",46.75],110:["ยาสระผม",120.00]}


def pricelist():
   z = "PRICE LIST"
   print("-"*80)
   print(z.center(80))
   print("-"*80)
   print("101: สบู่ 24.50 บาท          102: ผงซักฟอก 27.50 บาท        103: น้ำดื่ม 8.50 บาท ")
   print("104: แปรงสีฟัน 35.00 บาท     105: ยาสีฟัน 60.75 บาท          106: แป้งเด็ก 32.50 บาท ")
   print("107: บะหมี่่ 6.25 บาท         108: ข้าวสาร 185.00 บาท         109: น้ำมันพืช 46.75 บาท ")
   print("110: ยาสระผม 120.00 บาท")
   print("-"*80)




def login():
   loginprint = ("ยินดีต้อนรับสู่ระบบ LOGIN")
   print("-"*80)
   gg = loginprint.upper().center(90)
   print(gg)


   loop = 'true'
   while(loop == 'true'):	# ทำการ ใช้ while เพื่อ ลูปหา username password ในระบบ
        print("-"*80)
        username = input("Enter your ID : ")
        password = input("Enter your PASSWORD : ")
        print("-"*80)
        if(username == "admin" and password == "1234"):
          print(" ")
          print("="*80)
          print('***** ID : [ ' + username,"] Login successfully!! *****")
          pricelist()
          sale2()

        elif username != "admin" and password != "1234":
            print("ดูเหมือนท่านยังไม่เป็นสมาชิก..ต้องการสมัครใหม่ใช่หรือไม่ ?")
            ask = input("'Y'= ใช่ , 'N' = ไม่ใช่ : ")

            if ask == 'Y' or ask == 'y':
                print("-" * 80)
                username1 = input("กรอก Username ที่ต้องการสมัคร : ")
                password1 = input("กรอก Password ที่ต้องการสมัคร : ")
                print("=" * 80)
                print("***** Successfully registered !! *****")
                print("=" * 80)
                while (loop == 'true'):  # ทำการ ใช้ while เพื่อ ลูปหา username password ในระบบ
                    username = input("Enter your ID : ")
                    password = input("Enter your PASSWORD : ")
                    print("-" * 80)
                    if username == username1 and password == password1:
                        print("=" * 80)
                        print('***** ID : [ ' + username, "] Login Successfully!! *****")
                        print("=" * 80)
                        qw = ("********** ยินดีต้อนรับสู่ menu2 **********")
                        qe = qw.center(90)
                        print(qe)
                        print(" ")
                        pricelist()
                        sale2()

                    else:
                        print("***** รหัสผ่านผิด กรอกรหัสใหม่ *****")
            else:
                loop = 'true'
                while (loop == 'true'):
                    print("-" * 80)
                    username = input("Enter your ID : ")
                    password = input("Enter your PASSWORD : ")
                    print("-" * 80)
                    if (username == "admin" and password == "1234"):
                        print('ล็อกอินสำเร็จ' + username)
                        loop = 'false'
                        loop1 = 'true'
                        while (loop1 == 'true'):
                            command = input(username + ">> ")
                            if (command == "exit"):
                                print('ออกจากระบบสำเร็จ')
                                break
                    else:
                        print("รหัสผ่านผิด ต้องการสมัคร User ใหม่หรือไม่ ?")
                        ask = input("'Y'= ใช่ , 'N' = ไม่ใช่ : ")
                        if ask == 'Y' or ask == 'y':
                            print("-" * 80)
                            username1 = input("กรอก Username ที่ต้องการสมัคร : ")
                            password1 = input("กรอก Password ที่ต้องการสมัคร : ")
                            print("=" * 80)
                            print('***** ID : [ ' + username, "] Successfully registered !! *****")
                            print("=" * 80)
                            sale2()

                            while (loop == 'true'):
                                username = input("กรอก Username ที่ต้องการสมัคร : ")
                                password = input("กรอก Password ที่ต้องการสมัคร : ")
                                print("=" * 80)
                                if username == username1 and password == password1:
                                    print('***** ID : [ ' + username, "] Login Successfully!! *****")
                                    print("=" * 80)
                                    pricelist()
                                    sale2()
                                    loop = 'false'
                                    loop1 = 'true'
                                    while (loop1 == 'true'):
                                        command = input("S = Shop , E = Exit " + username + " :  ")
                                        if (command == "E" or command == "e"):
                                            print('ออกจากระบบสำเร็จ')
                                            break
                                        else:
                                            sale2()
                                else:
                                    print("'" + command + "' คำสั่งผิด!")
                        else:
                            print("*** ป้อนรหัสใหม่ให้ถูกต้อง !! ***")
        else:
            print('รหัสผ่านผิด')

def sale2():

     total = 0
     proID = int(input("กรอกรหัสสินค้า : "))
     print(" ")
     while proID > 100:
         print("***", product[proID][0], product[proID][1], "บาท", "***")
         print(" ")
         qty = int(input("จำนวน : "))
         print(" ")
         total = total + (product[proID][1] * qty) * 0.90
         total2 = total + 200
         print("ราคารวม ", total, " บาท")
         print("-" * 80)
         print("*** หากต้องการคิดเงิน กด'99'ในช่องรหัสสินค้า ***")
         print("-" * 80)
         proID = int(input("กรอกรหัสสินค้า : "))
         print(" ")
         if proID == 99:
             print("-" * 80)
             cash = int(input("รับเงินสดจากลูกค้า : "))
             change = cash - total2
             print("ยอดรวมราคาสินค้า + ค่าสมัครสมาชิก : %d" % total2, "บาท")
             print("เงินทอน : %0.2f" % change, "บาท")
             if change < 0:
                 print("-" * 80)
                 cash = int(input("เงินสดไม่พอ รับเงินสดจากลูกค้าใหม่อีกครั้ง : "))
                 change = cash - total2
                 print("ยอดรวมราคาสินค้า + ค่าสมัครสมาชิก : %d" % total2, "บาท")
                 print("เงินทอน : %0.2f" % change, "บาท")
               # update for stamp
             if total >= 50:
                 stamp = total // 50
                 print("จำนวนแสตมป์ ", stamp, " ดวง")
                 cont1 = input("เลือกซื้อสินค้าต่อกดปุ่ม 'y' : ")
                 if cont1 == 'Y' or cont1 == 'y':
                     sale2()
                 else:
                     print("OH no")
login()