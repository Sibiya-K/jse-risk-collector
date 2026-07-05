from dotenv import load_dotenv
import os

load_dotenv()

TICKERS = ["NPN.JO", "SBK.JO", "MTN.JO", "AGL.JO", "FSR.JO"]
CONFIDENCE_LEVEL = float(os.getenv("CONFIDENCE_LEVEL", 0.95))
APP_NAME = os.getenv("APP_NAME", "JSE Risk Collector")
DATA_FOLDER = "data"
