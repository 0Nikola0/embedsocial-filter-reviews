import json


def load_reviews():
    json_file = open("reviews.json")
    reviews = json.load(json_file)
    return reviews
    

def sort_reviews(data: list | tuple, highest_first=True, min_rating=1, oldest_first=True, prioritize_text=0):
    if min_rating > 1:
        data = [i for i in data if i['rating'] >= min_rating]

    if prioritize_text:
        # Show reviews with text first
        rez = sorted(data, key= lambda x: (not(len(x['reviewText']) > 0), x['rating'] * highest_first, x['reviewCreatedOnTime'] * oldest_first))
    else:
        rez = sorted(data, key= lambda x: (x['rating'] * highest_first, x['reviewCreatedOnTime'] * oldest_first))
    
    return rez

