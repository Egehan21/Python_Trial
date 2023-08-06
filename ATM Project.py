#Can check the balance
#Can withdraw
#Can deposit
#Close the program

balance=10

while True:
    x=int(input("Ne yapmak istersiniz; 1: Balance, 2: Withdraw, 3: Deposit, 4: Quit,"))
    if x ==1:
        print(balance)
    if x ==2:
        o=int(input("Ne kadar çekmek istersiniz?"))
        if balance-o < 0:
            print("Hesabinizda bu bakiye mevcut degildir!")
        else:
            balance = balance-o
            print(o, "Kadar para çektiniz, kalan bakiyeniz:", balance)
    if x==3:
        y=int(input("Ne kadar yatirmak istersiniz?"))
        balance = balance+y
        print(y, "Kadar para yatirdiniz, yeni bakiyeniz:", balance)
    if x==4:
        print("ATM'den cikis yapiyorsunuz, tesekkur ederiz")
        break
    else:
        print("Lütfen 1 ile 4 arasi bir rakam girin ve yapmak istediginiz islemi secin")
           


