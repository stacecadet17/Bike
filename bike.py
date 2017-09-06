class Bike(object):
    def __init__(self, price, max_speed):
        self.miles = 0
        self.price = price
        self.max_speed = max_speed
    def displayinfo(self):
        print "Price is" + " " + str(self.price)
        print "speed is" + " " + str(self.max_speed)
        print self.miles
        return self
    def ride(self):
        print "Riding..."
        self.miles = self.miles + 10
        return self
    def reverse(self):
        if (self.miles - 5 >= 0):
            print "Reversing..."
            self.miles = self.miles - 5
        else:
            print "can't reverse anymore"
        return self

bike1 = Bike(200, 25)
bike2 = Bike(100, 30)

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().reverse().reverse().reverse().displayinfo()
