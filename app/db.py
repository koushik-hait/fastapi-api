import motor.motor_asyncio
from config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)

database = client.students

print('Connected to MongoDB...')

db = client[settings.MONGO_INITDB_DATABASE]
User = db.users
# Post = db.posts
# User.create_index([("email", pymongo.ASCENDING)], unique=True)
# Post.create_index([("title", pymongo.ASCENDING)], unique=True)