from dotenv import load_dotenv 
import os 

load_dotenv() 

class Settings: 
    API_KEY: str = os.getenv('API_KEY')
    ENDPOINT: str = os.getenv('ENDPOINT_URL')
    DEPLOYMENT_NAME : str = os.getenv('DEPLOYMENT_NAME')
settings = Settings() 
