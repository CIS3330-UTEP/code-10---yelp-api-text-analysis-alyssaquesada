from yelpapi import YelpAPI
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


api_key = "4wtkt44zd5q1qeysL8hrn1i6TfD_sOCU00bfy-GBHDh4MwUNPxuOP0ChkCK5Z_991dde1AC082jHlezVLLuUVrYpcuKeaiVtAkiRsFLzF_kGyJO9LjgdRz8_KNE0ZHYx"

yelp_api = YelpAPI(api_key)

#search_query 
search_term = "sushi"
search_location = "Honolulu, HI"
search_sort_by = "rating"  # best_match, rating, review_count, distance
search_limit = 20

search_results = yelp_api.search_query(term=search_term, location=search_location, sort_by=search_sort_by,limit=search_limit)
#print(search_results)

for business in search_results['businesses']:
    print(business['name'])
#    print(business['alias'])
#    print("\n")

#result_df = pd.DataFrame.from_dict(search_results['businesses'])
#print(result_df['alias'])
# makes csv >>> result_df.to_csv("inclass_yelpapi.csv")
id_for_reviews = "rb-sushi-honolulu"

#reviews_query

reviews_result = yelp_api.reviews_query(id=id_for_reviews)

#print(reviews_result)
analyzer = SentimentIntensityAnalyzer()
reviews_df = [pd.DataFrame.from_dict(reviews_result['reviews'])]
for review in reviews_result['reviews']:
   sentiment_score = analyzer.polarity_scores(review)
   print(review)
   #print(sentiment_score)
   print("\n")
   if sentiment_score['compound'] >= 0.05 :
        print("Positive")
 
   elif sentiment_score['compound'] <= - 0.05 :
        print("Negative")
 
   else :
        print("Neutral")

#reviews_df = [pd.DataFrame.from_dict(reviews_result['reviews'])]
#print(reviews_df['text'])
