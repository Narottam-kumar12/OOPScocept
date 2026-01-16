# intialize class
class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print("start executing attributes / data")
        self.id = 123
        self.salary = 50000
        self.destigation = "SDE"
        print("attributed/data have been initiated")

    def travel(self, destination):
        print("The travel methos was call manually")
        print(f"Employee is now travelling to {destination}")


# create an object/instance of class
sam = employee()

sam.travel("Kerala")
    