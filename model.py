# Importing the libraries
import numpy as np
import pickle
import pandas as pd
from nltk import ngrams
from nltk.tokenize import sent_tokenize
import nltk
import ssl

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

#preprocessing
df = pd.read_excel(r'CombinedData.xlsx', engine="openpyxl")
df1 = pd.DataFrame(df, index = df.index, columns = df.columns)

vectorizer = CountVectorizer(min_df=2, max_df=0.7, stop_words=stopwords.words('english'))
posts = vectorizer.fit_transform(df1['Sentence'].values.astype('U')).toarray()
transformed_posts = pd.DataFrame(posts)
df1=pd.concat([df,transformed_posts],axis=1)
X = df1.iloc[:, 2:].values
y = df1['Label']

#Splitting Training and Test Set
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
from deepforest import CascadeForestClassifier
model = CascadeForestClassifier(random_state = 1, use_predictor = "adaboost")
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
#Fitting model with training data
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

pickle.dump(model, open('model.pkl','wb'))

# Loading model to compare the results
model1 = pickle.load( open('model.pkl','rb'))
#print(model1.predict([["hello"]]))

res="hello"
temp_df = pd.DataFrame({res})
post = vectorizer.transform(temp_df[0]).toarray()
result = model.predict(post)
print(result)
