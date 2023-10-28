import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

data_file = "data_file.xlsx"

df = pd.read_excel(data_file)

# Remove blank rows
df = df.dropna(subset=["timeline"])

# Initialize sentiment intensity analyzer
sid = SentimentIntensityAnalyzer()

str1 = "utc+05:30"  # Time information to skip

for data in df:
    a = data.find(str1)
    if a == -1:  # If str1 is not found
        ss = sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k, ss[k])