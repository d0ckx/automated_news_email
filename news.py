import requests


class NewsFeed:
    """
    representing multiple news titles and links as a string
    """

    base_url = "https://newsapi.org/v2/everything?"
    api_key = "api"

    def __init__(self, interest, from_date, to_date, language="en"):
        self.language = language
        self.to_date = to_date
        self.from_date = from_date
        self.interest = interest

    def get(self):
        url = self._build_url()

        articles = self.get_articles(url)

        email_body = ""
        for article in articles:
            email_body = email_body + article["title"] + "\n" + article[
                "url"] + "\n\n"
        return email_body

    def get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content["articles"]
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&language={self.language}&" \
              f"apiKey={self.api_key}"
        return url


if __name__ == "__main__":
    newsfeed = NewsFeed(interest="nasa", from_date="2023-08-27",
                        to_date="2023-08-29", language="en")

    print(newsfeed.get())



