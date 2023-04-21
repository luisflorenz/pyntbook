# Creating and using functions

# ow much is Luis paid if he works 45 hours a week at x company, and his hourly wage is a rate of 10.50?

def compupay(hrs, r):
    agreg = hrs* r
    return agreg

hrs = 45
r = 10.5
hweek = 40 
normal_w= hweek* r
extra_hour = r * 1.5
h_extra  =  hrs - 40 
extra_w = h_extra * extra_hour

def salaryplus (normal_w, extra_w):
    real_salary = normal_w + extra_w
    return real_salary

if hrs > 40:
    x = salaryplus (normal_w, extra_w)
    print('Luis salary is: ', x)
else:
    y = compupay (hrs, r)
    print('Luis salary is: ' , y) 