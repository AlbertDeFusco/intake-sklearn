from intake import open_catalog

cat = open_catalog('models.yaml')

data = [
    85.5,  # Max temperature
    6,     # Month
    False, # Holiday
    True,  # Weekend
    True   # home game
]

def predict(model, data=data):
    y = model.predict([data])[0]
    return y

local_model = cat.local_model.read()
print(predict(local_model))


s3_model = cat.s3_model.read()
print(predict(s3_model))
