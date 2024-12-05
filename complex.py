class Complex:
    def __init__(self):
        self.real = input("Enter real no. : ")
        self.img = input("Enter Img no. : ")

    def Cal(self):
        res = f"{self.real} + {self.img}i"
        print (res)

com = Complex()
com.Cal()