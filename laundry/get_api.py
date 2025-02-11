import json

from lib.sdgb import sdgb_api
from lib.get import get

if __name__ == "__main__":
    print(get(input("API Name: "),int(input("User ID: "))))
