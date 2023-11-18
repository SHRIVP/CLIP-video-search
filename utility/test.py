import plyvel

db = plyvel.DB('../dbs/videometadata_index', create_if_missing=False)

for key, value in db.iterator():
    print(f"{key.decode('utf-8')} = {value.decode('utf-8')}")

db.close()
