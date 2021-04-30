import twint

search = input("What are you searching for brother?")

city = input("Where?")

c = twint.Config()

c.Search = search

c.Near = city

c.Limit = 30

c.Popular_tweet = True

twint.run.Search(c)



