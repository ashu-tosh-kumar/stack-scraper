import os

from src.config import config

if __name__ == "__main__":
    if config.ENV in [
        "production",
    ]:
        print("Starting the application server")
        os.system("python -m flask --app src.main run --host 0.0.0.0 --port 8000")
    else:
        print("Starting the application server")
        os.system("python -m flask --app src.main run --host 0.0.0.0 --port 8000 --debug")
