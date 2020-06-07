from sklearn.linear_model import PassiveAggressiveClassifier

pac = PassiveAggressiveClassifier(max_iter=50)


def train_model(a, b):
    pac.fit(a, b)
