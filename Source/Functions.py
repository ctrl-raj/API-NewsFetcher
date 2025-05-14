import requests
import time
import datetime



api_key = "6da2fd3f045f4b81b1539a84c3b500d9"


# Function to fetch news
def fetch(topic):
    global topic2
    topic2 = topic
    global all_headlines
    lang_dict = {
        "english":"en",
        "hindi":"hi",
        "spanish":"es",
        "french":"fr",
        "german":"de",
        "chinese":"zh",
        "russian":"ru"
    }
    #lang = lang_dict.get(language)
    print(f"[Fetching News Based on '{topic}'...]")
    url = f"https://newsapi.org/v2/everything?q={topic}&from={datetime.date.today}&sortBy=publishedAt&language=en&apiKey={api_key}"
    response = requests.get(url)
    print(f"ResponseCode: [{response.status_code}]")

    try:
        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])
            all_headlines = ""
            print("✅-✅-✅")
            print(f"\nTop {min(len(articles), 5)} results for '{topic}' on 2025-04-07: \n")
            for i, article in enumerate(articles[:5], 1):
                title = article.get("title")
                source = article.get("source",{}).get("name")
                url = article.get("url")
                all_headlines = all_headlines + f"{i}. {title}\n   Source: {source}\n   URL: {url}\n\n"

            return all_headlines

            # Saves News in "NewsApiDataBase.txt"


    except Exception as e:
        print(f"An error occurred -> {e}")

def save_news():
    with open("NewsApiDataBase.txt", "a", encoding="utf-8") as f:
        f.write(f"\n" + f"-" * 80 + f"\nSaved news on search '{topic2}'Saved on: {datetime.date.today()}\n{all_headlines}\n" + "-" * 80 + "\n")
        # 80 = width of view page

# Display saved news
def view_news():
    global saved_news
    with open("NewsApiDataBase.txt", "r") as f:
        saved_news = f.read()
    return saved_news



#def allheadlines_results():
    #results = all_headlines.get()
    #load_frame3(results)



