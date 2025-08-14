class employee:
    # magic method/dunder method
    def __init__(self):
        print("execution of constructor")
        self.name="kunal"
        self.salary="50,000"
        self.designation='HR'
        print("extinction of constructor")
    # creating an method 
    def report(self,high):
        print("method initilaisng")
        print(f'the person {self.name} reports to Mr {high}')

# creating an instance of employee class
sam=employee()