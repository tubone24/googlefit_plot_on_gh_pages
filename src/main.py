from google_auth import GoogleAuth


key_path = "secrets.json"
scopes = ["https://www.googleapis.com/auth/fitness.activity.read"]

google_auth = GoogleAuth(key_path, scopes)
print(google_auth.get_token())
