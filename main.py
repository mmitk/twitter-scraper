import twitter

f1 = open('access_token.txt','r')
access_token = f1.readline()
f1.close()

f2 = open('access_token_secret.txt','r')
access_token_secret = f2.readline()
f2.close()

f3 = open('consumer_key.txt','r')
consumer_key = f3.readline()
f3.close()

f4 = open('consumer_secret.txt','r')
consumer_secret = f4.readline()
f4.close()

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret= consumer_secret,
                  access_token_key= access_token,
                  access_token_secret= access_token_secret)

print(api)