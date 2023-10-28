# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from textblob import TextBlob

# Define the authors and their documents
authors = ["Hamilton", "Madison", "Disputed", "Jay", "Shared"]
federalist_by_author = {  # Replace with your actual data
    "Hamilton": "Text data for Hamilton...",
    "Madison": "Text data for Madison...",
    "Disputed": "Text data for Disputed...",
    "Jay": "Text data for Jay...",
    "Shared": "Text data for Shared..."
}

# Preprocess and analyze the text
author_tokens = {}
for author, text_data in federalist_by_author.items():
    # Tokenize the text and remove stopwords
    tokens = [word for word in word_tokenize(text_data) if word.isalpha() and word not in stopwords.words("english")]
    author_tokens[author] = tokens

# Calculate the word length distribution for each author
author_word_lengths = {}
for author, tokens in author_tokens.items():
    word_lengths = [len(word) for word in tokens]
    author_word_lengths[author] = word_lengths

# Perform sentiment analysis using TextBlob
sentiment_scores = {}
for author, text_data in federalist_by_author.items():
    blob = TextBlob(text_data)
    sentiment_scores[author] = blob.sentiment.polarity

# Plot the word length distributions
plt.figure(figsize=(12, 6))
for author in authors:
    fdist = FreqDist(author_word_lengths[author])
    fdist.plot(15, title=f"Word Length Distribution for {author}", cumulative=False)
plt.legend(authors)
plt.show()

# Display sentiment analysis results
for author, sentiment in sentiment_scores.items():
    print(f"Sentiment analysis for {author}: Sentiment Score = {sentiment}")