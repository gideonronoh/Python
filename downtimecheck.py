import requests
def is_instagram_down():
    url = "https://www.instagram.com//"
    response = requests.get(url)
def is_facebook_down():
    url = "https://www.facebook.com//"
    return response.status_code !=200
if _name_== "_main_":
    if is_instagram_down():
        print("Instagram is down")
    elif is_facebook_down():
        print("Facebook is down")</