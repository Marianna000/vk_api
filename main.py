import requests, json

VK_USER_ID = '51717048'
VK_TOKEN = 'vk1.a.EodmhRYjTH5K0HVF2005-0ejiiloWQ34Zzsz7SbSN2-OPGTEvdjY8a1sBcph5fgv5FkzTJDorOBT8Ofh0XA9dY-sAQxOeNuOVvxURsyDjVRE6k5fBGH57P0T-wWgqCkJ7imkJyJZFAqTwtPEsLZH2Lu0x3qo0zeiqr-eLLS_JcrpNZpR2LiUcxrPO2HFEb7n'

def get_photo_data(offset = 0, count = 10):
    api_vk = requests.get('https://api.vk.com/method/photos.getAll', params={
        'owner_id': VK_USER_ID,
        'access_token': VK_TOKEN,
        'offset': 0,
        'count': count,
        'photo_sizes': 0,
        'v': 5.103
    })
    return json.loads(api_vk.text)

def main():
    print(get_photo_data())

if __name__ == "__main__":
    main()