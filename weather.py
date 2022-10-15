
import requests,time
from pushbullet import Pushbullet
while 1:
  res = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Hajiganj,Chandpur&appid=aa46358ed9ccd49917b50e5b1bd95f59")
  data = res.json()
  how_much_cloud = data['clouds']['all']
  visibility = (data['visibility'] // 1000)
  temp = (float("{:.2f}".format(data['main']['temp'] - 273.15)))
  feels_temp = (float("{:.2f}".format(data['main']['feels_like'] - 273.15)))
  humidity = (data['main']['humidity'])
  
  try:sea_level_hpa = (data['main']['sea_level'])
  except:sea_level_hpa = (data['main']['pressure'])

  try:ground_pressure_hpa = (data['main']['grnd_level'])
  except:ground_pressure_hpa = (data['main']['pressure'])

  try:rain_b = data['rain']["1h"]
  except:rain_b = (0)

  try: wind_gust_ms = (data['wind']['gust'])
  except: wind_gust_ms = ('null')

  weather_situation = (data['weather'][0]['description'])
  wind_speed = (data['wind']['speed']) 
  wind_flow_deg = (data['wind']['deg']) 

  #shukuralam533
  data_send = f"https://maker.ifttt.com/trigger/weather1/with/key/bflJUaEbmWPtluWwCEyQh9T2L5bV42U4Hb5JYyJUkl6?value1={temp}&value2={feels_temp}&value3={humidity}"
  requests.get(data_send)

  #alamhasan5338
  data_send = f"https://maker.ifttt.com/trigger/weather2/with/key/fxFg8bM5-dESkRQycv2B5kimxDfBJHM6utCiw3WPMIF?value1={ground_pressure_hpa}&value2={sea_level_hpa}&value3={visibility}"
  requests.get(data_send)

  #alamhasan53382
  data_send = f"https://maker.ifttt.com/trigger/weather3/with/key/p_BKFJoUVUSTBhnlGW_2iyFhrpko1zRNJUOi7yS3Mqh?value1={weather_situation}&value2={rain_b}&value3={how_much_cloud}"
  requests.get(data_send)

  #hasanahmed5338@gmail.com
  data_send = f"https://maker.ifttt.com/trigger/weather4/with/key/pdaiwcfFUNi6P4q-m667WK6uXt18A_KkzoAqAjnGP7u?value1={wind_speed}&value2={wind_flow_deg}&value3={wind_gust_ms}"
  requests.get(data_send)

  api = "o.zwGvl5OXibqDbrZ9saWhpXRvoXevJvMH"
  pb = Pushbullet(api)
  pust = pb.push_note("Hajiganj Weather Data", "Send Ok")
  time.sleep(1800)
