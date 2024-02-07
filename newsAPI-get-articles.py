# import required packages 
import json
from newsapi import NewsApiClient
import json
import os
os.chdir("/Users/annanavarro/Desktop/Azure/")


# Read configuration from JSON file
with open('News-Sentiment/newsAPIkey.json', 'r') as file:
    config = json.load(file)
api_key = config['api']['key']

# /v2/ev-get-everything
'''
News API is a simple, easy-to-use REST API that returns JSON 
    search results for current and historic news articles
    published by over 80,000 worldwide sources.
    https://newsapi.org/

Everything /v2/everything - we index every recent news and blog 
    article published by over 50,000 different sources large and small,
    and you can search through them with this endpoint.
'''
# Initialize NewsApiClient with API key
newsapi = NewsApiClient(api_key)

# Defined topic list 
topic_list = ['technology AI ,technology artificial intelligence','artificial intelligence, AI',
              'future AI, future artificial intelligence','artificial intelligence news',
              'AI update,artifical intelligence update','AI announcement,artifical intelligence announcement ',
              'computer vision','AI market analysis', 'AItrends, artifical intelligence trends','artifical intelligence',
              'ai','NLP','natural language processesing','AI text analysis,artifical intelligence text analysis', 
              'AI speech,artifical intelligence speech','AI healthcare, artifical intelligence healthcare',
              'AI gaming, artifical intelligence gaming','AI finance,artifical intelligence finance',
              'object detection','autonomous vehichles','AI chatbot, artifical intelligence chatbot',
              'facial recongition','new AI,new artifical intelligence','machine learning','technology AI, tech AI','generative AI',
              'LLM, large language model','AI demand']
#topic = topic_list[0]


for topic_index, topic in enumerate(topic_list):
    top_headlines = newsapi.get_everything(
        q= topic,  # Selected topic 
        language='en',
        domains= ("businessinsider.com,forbes.com,www.cnbc.com,theguardian.com,bloomberg.com,\
                    finance.yahoo.com,nytimes.com,wsj.com,wired.com,investors.com,bbc.com,news.mit.edu,\
                    foxnews.com,cnn.com,theverge.com,economist.com,reuters.com,usatoday.com,nbcnews.com,yahoo.com")
                )
            # Domains to search within 


    # Process each article, extract relevant information
    articles_list = []
    for article in top_headlines['articles']:
        article_info = {
            'source': article['source'],
            'author': article['author'],
            'title': article['title'],
            'description': article['description'],
            'url': article['url'],
            'urlToImage': article['urlToImage'],
            'publishedAt': article['publishedAt'],
            'content': article['content'],
            'source': article['source']['name'],
        }
        articles_list.append(article_info)


    # Save the list of article dictionaries to a JSON file
    json_file_path = os.path.join("News-Sentiment/Articles", f'{topic}_articles.json')
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(articles_list, json_file, ensure_ascii=False, indent=4)
    print(f'Articles saved to {topic}_articles.json')








