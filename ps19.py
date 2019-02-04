#!/usr/bin/python3

# How many Sundays fell on the first of the month 
# during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def compute(year_N):
    """ Takes a year param and return the number of sundays that fell on the first of 
        month between 1 Jan 1901 and 30 Dec of year param. 

        Param: year_N (int) in the format : _ _ _ _ e.g. 2000 

        Returns: sunday_counts (int) . The number of sundays on first of months.
    """

    sunday_counts = 0 

    # 1st of month on Jan 1901 is a Tuesday 
    # variable keeps track of the first of month for the current month 
    first_of_month = 2
    # 1 - Mon, 2 - Tuesday, 3 - Wed ...
    current_month = 1 
    year = 1901
    # Jan - 1 . One-based indexing 

    
    while year <= year_N:
        
        # determines whether the year is a leap year 
        if year % 4 == 0 and year % 100 != 0:
            leapYear = True 
        elif year % 400 == 0:
            leapYear = True 
        else:
            leapYear = False         

        # loops through every month and keeps track of first_of_month 
        # if first of month is a Sunday (7), increment sundays count 
        while current_month <= 12:
            
            # if first_of_month of current month is a sunday, increment sundays count
            if first_of_month == 7:
                sunday_counts += 1 
            # first of month only takes value from 1 to 7 
            elif first_of_month > 7:
                first_of_month -= 7     

            if current_month in [4, 6, 9, 11]:
                # months with 30 days 
                # next month's first of month will be 2 days of the week later. 
                # E.g. April's 1st of month is Wed, May's 1st of month will be Fri 
                first_of_month_increment = 2 # 30 % 28
            elif current_month == 2:
                # february 
                if leapYear:
                    first_of_month_increment = 1 
                else:    
                    first_of_month_increment = 0
            else:
                # months with 31 days 
                first_of_month_increment = 3  # 31 % 28 

            # next month values 
            current_month += 1 
            first_of_month += first_of_month_increment

        # Finished looping from January of year to December
        # next year values:
        year += 1 
        current_month = 1 
        # first_of_month value will stay the same 

    return sunday_counts    

if __name__ == "__main__":
    print(compute(2000))