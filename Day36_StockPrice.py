
import requests
from twilio.rest import Client


VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_NAME = "TASLA"
COMPANY_NAME = "TESLA Inc"
NEWS_DOMAIN = "techcrunch.com,thenextweb.com"

TWILIO_SID = "AC1f913eae192250592e047415358b1758"
TWILIO_AUTH_TOKEN = "74030e89daa8bf65eb3aac27219d646b"

STOCK_API_KEY = "Y5HCP26UG61COI9U"
New_API_Key = "3c91cd4179ca42e683b7404877a8d532"
# # STEP1:USE https://www.alphavantage.co/documentation/daily?
# # When stock price increase/decrease by 5% between yesterday and the day before yesterday then print ("Get News

#  #TODO1. Get yesterday's closing stock price
# stock_param = {
#     "function":"TIME_SERIES_DAILY",
#      "symbol":STOCK_NAME,
#      "apikey":STOCK_API_KEY,

# }
# response = requests.get(STOCK_ENDPOINT, params=stock_param)

# print(response.json())


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()["Meta Data"]  # show all information about data 
data = r.json()["Time Series (Daily)"]    # show daily wise data 

#data_list = [new_item for item in list] its trick
data_list = [value for (key, value) in data.items()]  # here is data print print out key and value 
yesterday_list  = data_list[0]
yesterday_closing_price = yesterday_list["4. close"]
# print (yesterday_closing_price)

#TODO2: Get the day before yesterday's closing stock price
day_before_yesterday_list  = data_list[1]
daybefore_yesterday_closing_price = day_before_yesterday_list["4. close"]
# print(day_before_yesterday_list)
# print (daybefore_yesterday_closing_price)

#TODO3:- find the positive difference between 1 and 2 

difference = round(abs(float(yesterday_closing_price) -float(daybefore_yesterday_closing_price)),2) # abs will get positive value 
difference = float(yesterday_closing_price) -float(daybefore_yesterday_closing_price)
if difference > 1:
    up_down = "emoji"
else:
    up_down = "emoji"
# print(difference )

#TODO4:-  work out the percentage difference in price between closing price yesterday and closing price the day before yesterday 
diff_percent = (difference/float(yesterday_closing_price))* 100
# print(round(diff_percent,2))

#TODO5:- if TODO4 percentage is greater than 5 than print("Get News")

# if diff_percent>0.01:
#     news_params = {
#         "apiKey":New_APIkey,
#         "searchIn": COMPANY_NAME
#     }
#     new_response = requests.get(NEWS_ENDPOINT, params=news_params)
#     print(new_response.json())


 # STEP 2: Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY NAME 
    
#TODO 6-: Instead of printing ("Get News"), use the news API to get article related to the company name 
#if diff_percent>0.01:
news_params = {
    "apiKey":New_API_Key,
    "qInTitle": COMPANY_NAME,
   }
new_response = requests.get(NEWS_ENDPOINT, params=news_params)
article =new_response.json()["articles"]
#print(articles)

# TODO 7- Use python slice operator to create a list that contains the first 3 articles. Hint:https//stackoverflow.com

three_articles  = article[:3]      # here the print first three articles 
#print(three_articles)

       #STEP 3-: Use Twilio to send a separate message with each article's title and description to your phone number, 

#TODO.8 -Create a new list of the first 3 article's headline and description using list comprehension 
#new_item = "Headline : {article title}. \nBrief:{article description}"
#new_item for item in list  # Here the use dictionary comprehension 
# formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']} for article in three_articles"]  

# print(formatted_article)

# #TODO.9 Send each article as a separate message via Twilio. 

# client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# for article in formatted_article:
#     message = client.messages.create(
#         body =article, 
#         from = "+15167306982",
#         to = +919439970162
#     )



# Assuming three_articles is a list of dictionaries containing article data
# Define your list comprehension to format articles
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles[:3]]

# Print the formatted articles (optional)
print(formatted_articles)

# Assuming you've initialized the Twilio client and have the necessary credentials
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Iterate through formatted articles and send each one via Twilio
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="+9439970162",  # Make sure this is your Twilio phone number
        to="+919439970162"      # Replace with the recipient's phone number
    )

    print("Message sent successfully:", message.sid)

# Define the list containing the dictionary
# data_list = [{'1. open': '183.5500', '2. high': '184.6800', '3. low': '183.0400', '4. close': '183.4100', '5. volume': '3338196'}]

# # Access the first (and only) element of the list and then access the value associated with the key '4. close'
# closing_price = data_list[0]['4. close']

# # Print the closing price
# print("Closing price:", closing_price)
