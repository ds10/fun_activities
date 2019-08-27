#first you want to add the right packages we are using tm and redditextractor
#if you are using rstudio, then go on the package tab in the bottom right and click install, pick tm and redditExtractor)


library(RedditExtractoR)
library(tm)



#first grab any urls you want, you may want to grab a subreddit and loop through them, or use a single url like below
my_url = "https://www.reddit.com/r/49ers/comments/cqv761/jets_fan_in_denver_with_some_intel/"

#this is a redditextractor function
url_data = reddit_content(my_url)

#this is also a reddit extractor function, its graphing the url, but you may need to look into exactly what it is doing.
#it also creates a gml output, this can be opened in gephi if you want a play, its easy to get in to, but does take a little time getting used to
graph_object = construct_graph(url_data, plot=TRUE, "gephifile.gml")

#this grabs all the attributes for the content, if you want a poke then (after youve ran this line) go in the top left,
#look for data and press example_attr
example_attr = reddit_content(URL="https://www.reddit.com/r/49ers/comments/cqv761/jets_fan_in_denver_with_some_intel/")

#here are all the comments you want to analyse
example_attr$comment

#you then to mess about with something like this: https://rpubs.com/tsholliger/301914
#there are loads of technqies, maybe google sentiment analysis or something