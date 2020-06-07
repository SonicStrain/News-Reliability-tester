from train_model import pac
from train_news import tfidf_v
import pandas as pd

# Read the file

df1 = pd.read_csv('news_to_be_tested.csv')

# Extract the features

test_feature = tfidf_v.transform(df1)

# Predict the result

prediction = pac.predict(test_feature)

# Print the result

print(prediction)
