#
# hw10pr1.py
#
# name:
#

# First, the class definition
# Below, we define several useful objects of type Date
#  +++ keep those and/or add your own! +++


class Date(object):
    """A user-defined data structure that
       stores and manipulates dates.
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """Construct a Date with the given month, day, and year."""
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        s = "{:02d}/{:02d}/{:04d}".format(self.month, self.day, self.year)
        return s


    # Here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False


    def copy(self):
        """Returns a new object with the same month, day, year
           as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew


    def equals(self, d2):
        """Decides if self and d2 represent the same calendar date,
           whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month \
          and self.day == d2.day:
            return True
        else:
            return False


    def __eq__(self, d2):
        """Overrides the == operator so that it declares two of the same dates
            in history as ==.  This way , we don't need to use the awkward
            d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month \
          and self.day == d2.day:
            return True
        else:
            return False


    def isBefore(self, d2):
        '''isBefore will check to see if self is a Date that comes before
            d2. It will return True is self does come before d2 and false otherwise
        '''
        if self.year < d2.year:
            return False
        if self.year >= d2.year:
            if self.month > d2.month:
                return True
            if self.month <= d2.month:
                if self.day > d2.day:
                    return True
                if self.day <= d2.day:
                    return False
    

    def isAfter(self, d2):
        '''isAfter will check to see if self's date comes after d2's date.
            If the dates are equal or if d2's date comes before, isAfter will return
            False.
        '''
        if self.year > d2.year:
            return False
        if self.year <= d2.year:
            if self.month < d2.month:
                return True
            if self.month >= d2.month:
                if self.day < d2.day:
                    return True
                if self.day >= d2.day:
                    return False

    def tomorrow(self):
        fdays = 28 + self.isLeapYear()
        if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10:
            if self.day == 31:
                self.month = 1
                self.day = 1
            else:
                self.day += 1
        if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
            if self.day == 30:
                self.day = 1
                self.month += 1
            else:
                self.day += 1
        if self.month == 2:
            if self.day == 28:
                self.day = 1
                self.month += 1
            else:
                self.day += 1
        if self.month == 12:
            if self.day == 31:
                self.day = 1
                self.month = 1
                self.year += 1
            else: 
                self.day += 1

    def yesterday(self):
        fdays = 28 + self.isLeapYear()
        if self.month == 1:
            if self.day == 1:
                self.year -= 1
                self.day = 31
                self.month = 12
            else:  
                self.day -= 1
        if self.month == 3:
            if self.day == 1:
                self.day = 28
                self.month -= 1
            else:
                self.day -= 1
        if self.month == 2 or self.month == 4 or self.month == 6 or self.month == 8 or self.month == 9 or self.month == 11:
            if self.day == 1:
                self.day = 31
                self.month -= 1
            else:
                self.day -= 1
        if self.month == 5 or self.month == 7 or self.month == 10 or self.month == 12:
            if self.day == 1:
                self.day = 30
                self.month -= 1
            else:
                self.day -= 1

            

            
                
           
            
        
        

            




#
# be sure to add code for the Date class ABOVE--inside the class definition
#





#
# lots of dates to work with...
#
# The nice this about putting them here is that they get redefined with each run
#   of the software (and this is needed for testing!)
#

d = Date(11, 13, 2018)    # Today?
d2 = Date(12, 21, 2018)   # winter break
ny = Date(1, 1, 2018)   # new year
nd = Date(1, 1, 2020)   # new decade
nc = Date(1, 1, 2100)   # new century
graduation = Date(5, 15, 2022)   # alter to suit!
vacation = Date(5, 17, 2019)     # ditto ~ summer break!
sm1 = Date(10, 28, 1929)    # stock market crash
sn2 = Date(10, 19, 1987)    # another s.m. crash: Mondays in Oct. are risky...
