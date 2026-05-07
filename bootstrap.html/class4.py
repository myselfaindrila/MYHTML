class Vehicle:
    model=""
    brand=""
    def __init__(self,model,brand):
        self.brand=brand
        self.model=model
    def moveForward(self):
        print(self.brand+" Move Forward")

    def moveBackward(self):
        print("Move Backward")

    def stop(self):
        print("Stopped")

obj=Vehicle('X6','BMW')
obj.moveForward()