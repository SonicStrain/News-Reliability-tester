import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from train_model import train_model
from test_model import test_model

# read data from csv file as to train and read the labels

df = pd.read_csv('news_for_training.csv')
labels = df.label

# Split the data into tran and test set

x_train, x_test , y_train, y_test = train_test_split(df['text'], labels, test_size=0.2, random_state=
7)

# Extract the features to train the model

tfidf_v = TfidfVectorizer(stop_words='english', max_df=0.7)

tfidf_train = tfidf_v.fit_transform(x_train)
tfidf_test = tfidf_v.transform(x_test)

# Train the model

train_model(tfidf_train,y_train)

# Test the model

y_pred = test_model(tfidf_test)
score = accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')