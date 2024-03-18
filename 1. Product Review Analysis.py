# Objective:
# The aim of this assignment is to extract insights from product reviews 
# by using string manipulation to categorize and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter

#     Write a program that searches through a series of product reviews for 
# keywords such as "good", "excellent", "bad", "poor", and "average". Print 
# out each review with the keywords in uppercase so they stand out.

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
    ]

words = ["bad","good","excellent","poor","average"]

def keywordReplacer(wordList, reviewList):
    
    for review in reviewList:
        for word in wordList:
            if word.lower() in review.lower():
                # print(f"found {word}")
                uppercaseWord = word.upper()
                # print(uppercaseWord)
                print(review.lower().replace(word, uppercaseWord))
            
        else:
            continue

    

keywordReplacer(words, reviews)

# Task 2: Sentiment Tally

#     Develop a function that tallies the number of positive and negative words 
# in each review. Use a predefined list of positive and negative words to check against. 
# The function should return the count of positive and negative words for each review.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentimentChecker(reviews):
    posTally = 0
    negTally = 0
    for review in reviews:
        for word in positive_words:
            if word in review.lower():
                posTally += 1
            else:
                continue
        for word in negative_words:
            if word in review.lower():
                negTally += 1
            else:
                continue

    return posTally, negTally

posTally, negTally = sentimentChecker(reviews)
print(f"the positive sentiment tally in your reviews is {posTally}, and the negative sentiment tally in your reviews is {negTally}")

# Task 3: Review Summary

#     Implement a script that takes the first 30 characters of a review and appends "…" 
# to create a summary. Ensure that the summary does not cut off in the middle of a word.

x = 0

while x < len(reviews):
    charlimit = 30
    addChars = 0
    while (reviews[x])[charlimit + addChars] != " ":
        addChars +=1
    else:
        print((reviews[x])[:charlimit+addChars] + "...")
    x += 1
    