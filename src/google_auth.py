from google.oauth2 import service_account
from google.auth.transport.requests import Request

key_path = "secrets.json"
scopes=["https://www.googleapis.com/auth/fitness.activity.read"]


class GoogleAuth:
    def __init__(self, secret_path: str, scopes):
        self.secret_path = secret_path
        self.scopes = scopes
        self.credentials = self.authenticate()
        
    def authenticate(self):
        credentials = service_account.Credentials.from_service_account_file(
            self.secret_path, scopes=self.scopes
        )
        credentials.refresh(Request())
        return credentials
    
    def get_token(self):
        if self.credentials.valid is not False:
            return self.credentials.token
        else:
            self.credentials.refresh(Request())
            return self.credentials.token
