class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"{self.username} logged in.")

    def post(self, content):
        print(f"{self.username} posted: {content}")

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers

    def share_story(self, story):
        print(f"{self.username} shared a story: {story}")

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets

    def tweet(self, tweet):
        print(f"{self.username} tweeted: {tweet}")

insta_account = InstagramAccount("insta_user", "insta_pass", 1500)
insta_account.login()
insta_account.post("Hello Instagram!")
insta_account.share_story("My day at the beach")
print(f"Number of followers: {insta_account.number_of_followers}")

twitter_account = TwitterAccount("twitter_user", "twitter_pass", 300)
twitter_account.login()
twitter_account.post("Hello Twitter!")
twitter_account.tweet("Just had a great lunch!")
print(f"Number of tweets: {twitter_account.number_of_tweets}")