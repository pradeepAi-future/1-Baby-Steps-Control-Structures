class multifunction():

    def Subfields(items):
        for i in items:
            print(i)
   
    def OddEven():
        i = int(input("Enter a number: "))
        if i % 2 == 0:
            return f"{i} is an Even number"
        else:
            return f"{i} is an Odd number"
   
    def Eligible(age, gender):
        if gender.lower() == "male" and age > 20:
            return "ELIGIBLE"
        elif gender.lower() == "female" and age > 18:
            return "ELIGIBLE"
        else:
            return "NOT ELIGIBLE"
 
    def Percentage(Subject1, Subject2, Subject3, Subject4, Subject5):
        total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        percent = (total / 500) * 100
        print("Total:", total)
        print("Percentage:", percent)

    def Triangle(Height, Breadth, Height1, Height2, Breadth1):
        Area = (Height * Breadth) / 2
        Perimeter = Height1 + Height2 + Breadth1
        print("Area of Triangle:", Area)
        print("Perimeter of Triangle:", Perimeter)
