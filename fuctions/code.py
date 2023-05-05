# Creating and using functions

import math

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

#  Exercise - Data Analysis
#  You're planning a vacation, and you need to decide which city you want to visit. You have shortlisted four cities and identified the return flight cost, daily hotel cost, and weekly car rental cost. While renting a car, you need to pay for entire weeks, even if you return the car sooner.
#  If you're planning a 1-week long trip, which city should you visit to spend the least amount of money?
# 

def cost_of_trip(return_flight, hotel_day, car_rental_week):
    cost_week_trip = return_flight+ hotel_day+ car_rental_week
    return cost_week_trip

Paris_trip = cost_of_trip(
    return_flight= 200,
    hotel_day= 20*7,
    car_rental_week= 200
) 
print( Paris_trip)

London_trip = cost_of_trip(
    return_flight= 250,
    hotel_day= 30*7,
    car_rental_week= 120
)
print(London_trip)

Dubai_trip = cost_of_trip(
    return_flight= 370,
    hotel_day= 15*7,
    car_rental_week= 80
)
print(Dubai_trip)

Mumbai_trip = cost_of_trip(
    return_flight=  450,
    hotel_day= 10*7,
    car_rental_week= 70
)
print(Mumbai_trip)

countries_trip_cost= (Paris_trip, London_trip, Dubai_trip, Mumbai_trip )
print(countries_trip_cost)
cheaper_trip = min(countries_trip_cost)


print('the country to spend the least amount of money is london because their cost is: ', cheaper_trip )

# How does the answer to the previous question change if you change the trip's duration to four days, ten days or two weeks?

# Trip for four days


def cost_of_trip(return_flight, hotel_day, car_rental_week):
    cost_week_trip = return_flight+ hotel_day+ car_rental_week
    cost_week_trip = math.ceil(cost_week_trip)
    return cost_week_trip

day_trip_Paris = cost_of_trip(
    return_flight= 200,
    hotel_day= 20*4,
    car_rental_week=  (200/7)*4
)
print('The cost of the Paris trip for four day is: ', day_trip_Paris)

day_trip_London = cost_of_trip(
    return_flight= 250,
    hotel_day=  30*4,
    car_rental_week= (120/7)*4
)
print('The cost of the London trip for four days is:  ', day_trip_London)

day_trip_Dubai = cost_of_trip(
    return_flight=370,
    hotel_day= 15*4,
    car_rental_week= (80/7)*4
)
print('The cost of the Dubai trip for four days is: ', day_trip_Dubai)

day_trip_Mumbai = cost_of_trip(
    return_flight=450,
    hotel_day= 10*4,
    car_rental_week= (70/7)*4
)
print('the cost of the Mumbai trip is: ', day_trip_Mumbai)

# trip for ten day

ten_day_Paris_trip = cost_of_trip(
    return_flight= 200,
    hotel_day= 20*10,
    car_rental_week= (200/7)*10
)
print('The cost to the Paris trip for 10 days is: ', ten_day_Paris_trip)

ten_day_London_trip = cost_of_trip(
    return_flight=250,
    hotel_day=30*10,
    car_rental_week=(250/7)*10
)
print('The cost to the London trip for ten days is: ', ten_day_London_trip)

ten_day_Dubai_trip= cost_of_trip(
    return_flight=370,
    hotel_day=15*10,
    car_rental_week=(80/7)*10
)
print('The cost to the Dubai trip for ten days is: ', ten_day_Dubai_trip)

ten_day_Mumbai= cost_of_trip(
    return_flight=450,
    hotel_day=10*10,
    car_rental_week=(70/7)*10
)
print('The cost to the Mumbai trip for ten days is: ', ten_day_Mumbai)

# trip for two weeks

week_trip_Paris= cost_of_trip(
    return_flight=200,
    hotel_day=20*14,
    car_rental_week=200*2
)
print('The cost to the Paris trip for two weeks is: ', week_trip_Paris)


week_trip_london= cost_of_trip(
    return_flight=250,
    hotel_day=30*14,
    car_rental_week=120*2
)
print('The cost to the London trip for two weeks is: ', week_trip_london)

week_trip_Dubai= cost_of_trip(
    return_flight=370,
    hotel_day=15*14,
    car_rental_week=80*2
)
print('The cost to the Dubai trip for two weeks is: ', week_trip_Dubai)

week_trip_Mumbai= cost_of_trip(
    return_flight=450,
    hotel_day=10*14,
    car_rental_week=70*2
)
print('The cost to the Mumbai trip for two weeks is: ', week_trip_Mumbai)

# If your total budget for the trip is $1000, which city should you visit to maximize the duration of your trip? Which city should you visit if you want to minimize the duration?

day_trip_Paris_2 = cost_of_trip(
    return_flight=200,
    hotel_day= 20*16,
    car_rental_week=(200/7)*16
)
print(day_trip_Paris_2)

day_trip_London_2 = cost_of_trip(
    return_flight= 250,
    hotel_day=  30*15,
    car_rental_week= (120/7)*15
)
print(day_trip_London_2)

day_trip_Dubai_2= cost_of_trip(
    return_flight=370,
    hotel_day=15*23,
    car_rental_week=(80/7)*23
)
print(day_trip_Dubai_2)

day_trip_Mumbai_2= cost_of_trip(
    return_flight=450,
    hotel_day=10*27,
    car_rental_week=(70/7)*27
)
print(day_trip_Mumbai_2)


print('If my budget is 1000 $, the trip that gives more days is the trip to Mumbai because for 27 days I will spend: ', day_trip_Mumbai_2 )

print('If my budget is 1000 $, the trip that gives less days is the trip to London because for 15 days I will spend: ', day_trip_London_2 )

# How does the answer to the previous question change if your budget is $600, $2000, or $1500?

# if the bubget is 600

day_trip_Paris_3= cost_of_trip(
    return_flight=200,
    hotel_day=20*8,
    car_rental_week=(200/7)*8
)
print(day_trip_Paris_3)

day_trip_London_3= cost_of_trip(
    return_flight=250,
    hotel_day=30*7,
    car_rental_week=120
)
print(day_trip_London_3)

day_trip_Dubai_3= cost_of_trip(
    return_flight=370,
    hotel_day=15*8,
    car_rental_week=(80/7)*8
)
print(day_trip_Dubai_3)

day_trip_Mumbai_3= cost_of_trip(
    return_flight=450,
    hotel_day=10*7,
    car_rental_week=70
)
print(day_trip_Mumbai_3)

print('If my budget is 600 $, the trip that gives more days are the trip to Paris and Dubai because for 8 days I will spend: ', 'Paris: ', day_trip_Paris_3, 'Dubai:', day_trip_Dubai_3)
print('If my budget is 600 $, the trip that gives less days are the trip to London and Mumbai because a week days I will spend: ', 'London: ', day_trip_London_3, 'Mumbai:', day_trip_Mumbai_3)

# if the budget is 1500

day_trip_Paris_4= cost_of_trip(
    return_flight=200,
    hotel_day=20*26,
    car_rental_week=(200/7)*26
)    
print(day_trip_Paris_4)

day_trip_London_4= cost_of_trip(
    return_flight=250,
    hotel_day=30*26,
    car_rental_week=(120/7)*26
)
print(day_trip_London_4)

day_trip_Dubai_4= cost_of_trip(
    return_flight=370,
    hotel_day=15*42,
    car_rental_week=(80/7)*42
)
print(day_trip_Dubai_4)

day_trip_Mumbai_4= cost_of_trip(
    return_flight=450,
    hotel_day=10*52,
    car_rental_week=(70/7)*52
)
print(day_trip_Mumbai_4)

print('If my budget is 1500 $, the trip that gives more days is the trip to Mumbai because for 52 days I will spend: ',  day_trip_Mumbai_4)
print('If my budget is 1500 $, the trip that gives less days are the trip to Paris and London because for 26 days I will spend: ', 'Paris:', day_trip_Paris_4, 'Dubai:', day_trip_London_4)



# if rhe budget is 2000

day_trip_Paris_5= cost_of_trip(
    return_flight=200,
    hotel_day=20*37,
    car_rental_week=(200/7)*37
)
print(day_trip_Paris_5)

day_trip_London_5= cost_of_trip(
    return_flight=250,
    hotel_day=30*37,
    car_rental_week=(120/7)*37
)
print(day_trip_London_5)

day_trip_Dubai_5= cost_of_trip(
    return_flight=370,
    hotel_day=15*61,
    car_rental_week=(80/7)*61
)
print(day_trip_Dubai_5)

day_trip_Mumbai_5= cost_of_trip(
    return_flight=450,
    hotel_day=10*77,
    car_rental_week=(70/7)*77
)
print(day_trip_Mumbai_5)

print('If my budget is 2000 $, the trip that gives more days are the trip to Mumbai because for 77 days I will spend: ', day_trip_Mumbai_5)
print('If my budget is 2000 $, the trip that gives less days are the trip to Paris and London because for 37 days I will spend: ', 'Paris:', day_trip_Paris_5, 'London:', day_trip_London_5)


# other for to solve the problem using fuction

Paris = [200, 20, 200, 'Paris']
London = [250, 30, 120, 'London']
Dubai = [370, 15, 80, 'Dubai']
Mumbai =  [450, 10, 70, 'Mumbai']
Cities = [Paris, London, Dubai, Mumbai ]

def cost_of_the_trip(flight, hotel_cost, car_rent, num_of_days=0):
    return flight+(hotel_cost*num_of_days)+(car_rent*math.ceil(num_of_days/7))

def day_to_visit(days):
    costs=[]
    for city in Cities:
        cost=cost_of_the_trip(city[0],city[1],city[2],days)
        costs.append((cost,city[3]))
    min_cost = min(costs)
    return min_cost    

#  If you're planning a 1-week long trip, which city should you visit to spend the least amount of money?
#
day_to_visit(7)  
print(day_to_visit(7))

# 2- How does the answer to the previous question change if you change the trip's duration to four days, ten days or two weeks?

print(day_to_visit(4))
print(day_to_visit(10))
print(day_to_visit(14))


# 3- If your total budget for the trip is $600, which city should you visit to maximize the duration of your trip? Which city should you visit if you want to minimize the duration?

def given_budget(budget, less_days=False):
    days=1
    cost=0
    while cost<budget:
        #copy of the city cost
        cost_before=cost
        try:
            #copy of costs dictionary, if exists
            costs_before=costs.copy()
        except:
            # if costs dictionary dosen't  exist, create an empty dictionary
            costs_before={}
        costs={}
        for city in Cities:
            cost=cost_of_the_trip(city[0],city[1],city[2],days)
            costs[cost] = city[3]
        if less_days:
            cost=max(list(costs.keys()))
            ''' The while loop breaks only after cost>600 condition is met.
            when the condition is met, the costs dictionary updates to values that are greater than 600 
            so we check if it is exceeding, if it does, we return the values from the previous dictionary cost_before. '''
            if cost>=budget:
                return costs_before[cost_before],days-1
        else:
            cost=min(list(costs.keys()))
            if cost>=budget:
                return costs_before[cost_before],days-1
                
        days+=1    


city_to_stay_maximum_days=given_budget(600)
print(city_to_stay_maximum_days) 

city_to_stay_minimum_days=given_budget(600, less_days=True)
print(city_to_stay_minimum_days)
                
# How does the answer to the previous question change if your budget is $1000, $2000, or $1500?

# for 1000 dollars

city_to_stay_maximum_days=given_budget(1000)
print(city_to_stay_maximum_days)

city_to_stay_minimum_days=given_budget(1000, less_days=True)
print(city_to_stay_minimum_days)

# for 2000 dollars

city_to_stay_maximum_days=given_budget(2000)
print(city_to_stay_maximum_days)

city_to_stay_minimum_days=given_budget(2000, less_days=True)
print(city_to_stay_minimum_days)

# for 1500 dollars

city_to_stay_maximum_days=given_budget(1500)
print(city_to_stay_maximum_days)

city_to_stay_minimum_days=given_budget(1500, less_days=True)
print(city_to_stay_minimum_days)


# trie another example

# How is the salary of Pedro of march f he work 2  holidays

salary_per_hour = 108
work_day = 5
working_hours_per_week= work_day*salary_per_hour 



def montly_salary(salary_per_hours, working_hours_per_week):
    return salary_per_hours*working_hours_per_week*4
#if working_hours_per_week < 40:
#overtime_salary= salary_per_hour* 2.69
#extra= overtime_salary + montly_salary
print('The pedro salary is: ', montly_salary(108, 40))



#def extra_holi_salary(salary_holiday):
    #salary_holiday = salary_per_hour*2
    #h_day = 2
    #holiday_day= work_day- h_day
    #holi_salary= salary_holiday*holiday_day 
    #return montly_salary - holiday_day 
    
    
        
#print("{} is aged {}, and owns an {}.".format(
    #person["Name"], 
    #person["Age"], 
    #"Android phone" if person["HasAndroidPhone"] else "iPhone"
#))   


a_range= range(3,9)

a_list= list(a_range)
print(a_list) 

a1_lsit= list()
for x in a_range:
    a1_lsit.append(x)
print(a1_lsit) 

#a3_range = range(18, 535)
#a3_list = list(a3_range)
#print(a3_list)

#sum_of_number= 0
#for r in a3_list:
    #if r %7 ==0:
        #sum_of_numbers += r

#num= dict(r, end='')
#print(num)

total=0
n=18


while n<534:
    if not n%7:
        total+=n
    n+=1
print ('The sum of all the numbers divisible by 7 between 18 and 534 is {}.'.format(total))
    

sum_of_numbers = 0
r = 18

while r<534:
    if not r%7:
        sum_of_numbers += r
    r+=1
print('The sum of all the numbers divisible by 7 between 18 and 534 is {}.'.format(sum_of_numbers))           

' A travel company wants to fly a plane to the Bahamas. Flying the plane costs 5000 dollars. So far, 29 people have signed up for the trip. If the company charges 200 dollars per ticket, what is the profit made by the company?'  

cost_of_flying_plane =  5000
numbers_of_passanger = 29
price_of_ticket = 200
profit = numbers_of_passanger * price_of_ticket - cost_of_flying_plane
print('the company makes of a profitof {} dollars'.format(profit))

return_flight = numbers_of_passanger - 17
profit_return_flight = return_flight * price_of_ticket - cost_of_flying_plane
print(profit_return_flight)

tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]

number_of_tweets = len(tweets)
print(number_of_tweets)

happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']
sample_tweet = tweets[0]
print(sample_tweet)

is_tweet_happy = False

# Get a word from happy_words
for word in happy_words:
    # Check if the tweet contains the word
    if word in sample_tweet:
        # Word found! Mark the tweet as happy
        is_tweet_happy = True

print(is_tweet_happy)   

'Determine the number of tweets in the dataset that can be classified as happy'

cont = 0

for words in tweets:
    words= words.rstrip()
    #print(words)
    if  words == happy_words:
        continue
    print(words)
    word= words.split()
    tot= len(word)
    number_of_happy_tweets= cont + tot
print('the total of happy tweets are: ', number_of_happy_tweets)    

    
   

' What fraction of the total number of tweets are happy?'

happy_fraction = number_of_happy_tweets/10
print("The fraction of happy tweets is:", happy_fraction)

'Determine the number of tweets in the dataset that can be classified as sad.'

number_of_sad_tweets = 0
is_tweet_sad = False

for st in tweets:
    for word in sad_words:
        if word in st:
            is_tweet_sad = True
            if is_tweet_sad == True:
                number_of_sad_tweets += 1
                
print('the total of sad tweets are: ', number_of_sad_tweets) 



'What fraction of the total number of tweets are sad?'

sad_fraction = number_of_sad_tweets/10
print("The fraction of sad tweets is:", sad_fraction)

' Calculate the sentiment score, which is defined as the difference betweek the fraction of happy tweets and the fraction of sad tweets.'
sentiment_score = happy_fraction - sad_fraction
print("The sentiment score for the given tweets is", sentiment_score)

'this is a example menssage for get the commit'
'this is another example menssage for get the commit'








