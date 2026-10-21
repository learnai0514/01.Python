class multiFunctions:
    def Subfields():
        fields = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for fi in fields:
            print(fi)

    def OddEven():
        num = int(input("Enter a Number"))
        if(num % 2 == 1):
            print(num, " Number is Odd Number") 

    def Elegible():
        gender = input("Your Gender")
        age = int(input("Your Age"))
        if (gender == "Male"):
            if(age <21):
                print("Not Eligible")
            else:
                print("Eligible")
        else:
            if(age<18):
                print("Not Eligible")
            else:
                print("Eligible")

    def percentage():
        marks = [85,25,89,45,34]
        total=0
        for index,m in enumerate(marks,1):
            print(f"Subjects",index, "=", m)
            total +=m
        print("Total=",total);
        print("Average=", total/len(marks))

    def triangle(height,breadth,height1,height2,breadth2):
        print("Height:",height)
        print("Breadth:",breadth)
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", (height*breadth)/2)
        print("Height1:", height1)
        print("Height2:", height2)
        print("Breadth:", breadth2)
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", height1+height2+breadth2)
        