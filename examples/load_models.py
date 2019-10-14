from intake import open_catalog

cat = open_catalog('models.yaml')

local_model = cat.local_model.read()
print(local_model)

s3_model = cat.s3_model.read()
print(s3_model)
