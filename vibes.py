from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

movie_reviews = [
    "A bad love story. Don't watch this. filled with butt, German and computer Jokes.",
    "The movie was grand. Definitely was not what I was expecting some parts were a little weird but we've seen that with SpongeBob over the years. However overall I would definitely recommend this to another. A solid movie that I very much enjoyed.",
    "A massive improvement over the sandy movie, plankton the movie keeps all the charm spongebob is known for in tact.",
    "Ok why was this genuinely really damn good",
    "New animation stinks",
    "Don't waste your time, now a good movie",
    "I did not like this movie. The humor is not funny and the story is not good."
]

labels = [
    'negative', 'positive', 'positive', 'positive', 'negative', 'negative', 'negative'
]

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(movie_reviews)

x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)

print('Accuracy:', accuracy)

if accuracy > 0.8:
  print('Good vibes. Book the ticket!')
else:
  print('Needs more work!')