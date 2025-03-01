import json

from sdgb import sdgb_api
from musicdata import userId

def get(api_name,userId):
    data = json.dumps({
        "userId": int(userId)
    })

    get_result = sdgb_api(data, api_name, userId)

    return get_result

if __name__ == "__main__":
    api_name = "GetUserPreviewApi"
    print(get(api_name,userId))