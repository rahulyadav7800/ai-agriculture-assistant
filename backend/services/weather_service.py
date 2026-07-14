import httpx

from backend.utils.logger import logger


class WeatherService:

	def __init__(self):

		self.weather_url = "https://api.open-meteo.com/v1/forecast"

		self.reverse_url = "https://nominatim.openstreetmap.org/reverse"

		self.timeout = httpx.Timeout(
			connect=15,
			read=30,
			write=30,
			pool=15
		)

	async def _get_city(

		self,

		client: httpx.AsyncClient,

		latitude: float,

		longitude: float

	) -> str:

		try:

			response = await client.get(

				self.reverse_url,

				params={

					"lat": latitude,

					"lon": longitude,

					"format": "jsonv2"

				},

				headers={

					"User-Agent": "AI-Agriculture-Assistant"

				}

			)

			response.raise_for_status()

			data = response.json()

			address = data.get(
				"address",
				{}
			)

			return (

				address.get("city")

				or address.get("town")

				or address.get("village")

				or address.get("county")

				or "Unknown"

			)

		except Exception:

			return "Unknown"

	async def get_weather(

		self,

		latitude: float,

		longitude: float

	) -> dict:

		params = {

			"latitude": latitude,

			"longitude": longitude,

			"current": ",".join([

				"temperature_2m",

				"relative_humidity_2m",

				"apparent_temperature",

				"wind_speed_10m",

				"weather_code"

			]),

			"hourly": "precipitation_probability",

			"forecast_days": 1

		}

		try:

			async with httpx.AsyncClient(

				timeout=self.timeout

			) as client:

				weather_response = await client.get(

					self.weather_url,

					params=params

				)

				weather_response.raise_for_status()

				weather_data = weather_response.json()

				city = await self._get_city(

					client,

					latitude,

					longitude

				)

			current = weather_data["current"]

			hourly = weather_data["hourly"]

			rain_probability = 0

			for index, hourly_time in enumerate(

				hourly["time"]

			):

				if hourly_time[:13] == current["time"][:13]:

					rain_probability = hourly[
						"precipitation_probability"
					][index]

					break

			return {

				"temperature": current["temperature_2m"],

				"feels_like": current["apparent_temperature"],

				"humidity": current["relative_humidity_2m"],

				"wind_speed": current["wind_speed_10m"],

				"rain_probability": rain_probability,

				"weather_code": current["weather_code"],

				"condition": self._weather_condition(

					current["weather_code"]

				),

				"city": city

			}

		except Exception as error:

			logger.exception(error)

			return {

				"temperature": None,

				"feels_like": None,

				"humidity": None,

				"wind_speed": None,

				"rain_probability": None,

				"weather_code": None,

				"condition": "Unknown",

				"city": "Unknown"

			}

	def _weather_condition(

		self,

		code: int

	) -> str:

		conditions = {

			0: "Clear Sky",

			1: "Mainly Clear",

			2: "Partly Cloudy",

			3: "Overcast",

			45: "Fog",

			48: "Depositing Rime Fog",

			51: "Light Drizzle",

			53: "Moderate Drizzle",

			55: "Dense Drizzle",

			61: "Light Rain",

			63: "Moderate Rain",

			65: "Heavy Rain",

			71: "Light Snow",

			73: "Moderate Snow",

			75: "Heavy Snow",

			80: "Rain Showers",

			81: "Heavy Rain Showers",

			82: "Violent Rain Showers",

			95: "Thunderstorm",

			96: "Thunderstorm With Hail",

			99: "Severe Thunderstorm"

		}

		return conditions.get(

			code,

			"Unknown"

		)


weather_service = WeatherService()