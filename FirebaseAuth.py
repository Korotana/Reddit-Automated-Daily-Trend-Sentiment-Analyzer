import firebase_admin
from firebase_admin import credentials, db

service_account_Json_filepath = r"C:\Users\YuvrajKorotana\PycharmProjects\PythonAutomationScriptforCloudServices\service-account.json"
# Path to your downloaded JSON file
cred = credentials.Certificate(service_account_Json_filepath)

# Initialize Firebase Admin SDK with Realtime Database URL
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://twittertrendinghashtag-product-default-rtdb.firebaseio.com/'  # Replace with your actual database URL
})


ref = db.reference('trending')
ref.set({"product": "example_product", "mentions": 100})