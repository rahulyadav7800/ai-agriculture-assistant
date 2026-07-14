import httpx

from backend.utils.logger import logger


class WeatherService:

	def __init__(self):

		self.base_url = "https://api.open-meteo.com/v1/forecast"

		self.timeout = httpx.Timeout(
			connect=15,
			read=30,
			write=30,
			pool=15
		)

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

				response = await client.get(
					self.base_url,
					params=params
				)

				response.raise_for_status()

				data = response.json()

			current = data["current"]

			hourly = data["hourly"]

			rain_probability = None

			for i, hourly_time in enumerate(hourly["time"]):

				if hourly_time[:13] == current["time"][:13]:

					rain_probability = hourly[
						"precipitation_probability"
					][i]

					break

			if rain_probability is None:

				rain_probability = 0

			return {

				"temperature": current["temperature_2m"],

				"feels_like": current["apparent_temperature"],

				"humidity": current["relative_humidity_2m"],

				"wind_speed": current["wind_speed_10m"],

				"rain_probability": rain_probability,

				"condition": self._weather_condition(
					current["weather_code"]
				)
			}

		except Exception as error:

			logger.exception(error)

			return {
				"temperature": None,
				"feels_like": None,
				"humidity": None,
				"wind_speed": None,
				"rain_probability": None,
				"condition": "Unknown"
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