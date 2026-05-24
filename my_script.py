import text_analyzer

datacamp_tweets = """
Excited to start learning Python today with @DataCamp! #DataScience #Python
Shoutout to @DataCamp for the amazing software engineering course. #Coding #LearnPython
Can't believe how easy it is to build text analysis packages with @DataCamp! #Python #NLP
Working on a custom social media analyzer tool. @DataCamp makes it fun. #DataScience
Loving this new exercise on class inheritance. @DataCamp is the best! #OOP #Python
"""


# Create a SocialMedia instance with datacamp_tweets
dc_tweets = text_analyzer.SocialMedia(text=datacamp_tweets)

# Print the top five most mentioned users
print(dc_tweets.mention_counts.most_common(5))

# Plot the most used hashtags
text_analyzer.plot_counter(dc_tweets.hashtag_counts)