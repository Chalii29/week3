class Python_switch:
    def day(self, month):

        default = "Incorrect day"

        return getattr(self,'case_' + str(month), lambda: default)()
    
    def case_1(self):
        return "Jan"
    def case_2(self):
        return "Feb"
    def case_3(self):
        return "Mar"
switch = Python_switch()

print (switch.day(1))
print (switch.day(2))
print (switch.day(3))
    