#! python3 
# By considering the terms in the Fibonacci sequence whose values do 
# not exceed four million, find the sum of the even-valued terms.

def compute():
    total = 2 #includes 2nd term 
    x1 = 1 
    x2 = 2 
    y = x1 + x2 

    # value does not exit 4 million 
    while y < 4000000:
        # if value even, add to total 
        if y % 2 == 0:
            total += y 

        # computing value of next term     
        x1 = x2 
        x2 = y
        y = x1 + x2 
        
    return total 

if __name__ == "__main__":
	print(compute())    

