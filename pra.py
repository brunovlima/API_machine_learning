import pickle

file = open('irishtopickle.pkl', 'rb')
model = pickle.load(file)

pdf = model.predict([[4, 2, 6, 0]])
print(pdf)
