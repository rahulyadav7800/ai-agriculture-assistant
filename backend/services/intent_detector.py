from enum import Enum


class Intent(str, Enum):
	PLANT_IDENTIFICATION = "plant_identification"
	DISEASE_DIAGNOSIS = "disease_diagnosis"
	PLANT_HEALTH = "plant_health"
	WATERING = "watering"
	FERTILIZER = "fertilizer"
	GROWTH_ADVICE = "growth_advice"
	PRUNING = "pruning"
	PEST_CONTROL = "pest_control"
	HARVESTING = "harvesting"
	SOIL_MANAGEMENT = "soil_management"
	SUNLIGHT = "sunlight"
	TEMPERATURE = "temperature"
	HUMIDITY = "humidity"
	PROPAGATION = "propagation"
	REPOTTING = "repotting"
	FLOWERING = "flowering"
	FRUITING = "fruiting"
	SEED_INFORMATION = "seed_information"
	NUTRIENT_DEFICIENCY = "nutrient_deficiency"
	TOXICITY = "toxicity"
	WEED_MANAGEMENT = "weed_management"
	CROP_RECOMMENDATION = "crop_recommendation"
	COMPANION_PLANTING = "companion_planting"
	SEASONAL_CARE = "seasonal_care"
	WEATHER_ADVICE = "weather_advice"
	GENERAL_QUESTION = "general_question"
	DEFAULT_ANALYSIS = "default_analysis"


class IntentDetector:
	"""
	Rule-based intent detector.

	Fast, deterministic and easily replaceable with
	a hybrid (Rule + LLM) classifier in the future.
	"""

	def __init__(self):
		self.intent_keywords = {

			Intent.PLANT_IDENTIFICATION: [
				"identify",
				"identify plant",
				"identify this",
				"which plant",
				"what plant",
				"plant name",
				"name of this plant",
				"scientific name",
				"species",
				"plant identification"
			],

			Intent.DISEASE_DIAGNOSIS: [
				"disease",
				"infected",
				"infection",
				"fungus",
				"fungal",
				"virus",
				"viral",
				"bacteria",
				"bacterial",
				"yellow leaves",
				"brown leaves",
				"black spots",
				"leaf curl",
				"wilting",
				"dry leaves",
				"leaf drop",
				"stem rot",
				"root rot",
				"problem",
				"what happened"
			],

			Intent.PLANT_HEALTH: [
				"healthy",
				"health",
				"is it healthy",
				"overall health",
				"plant condition",
				"condition"
			],

			Intent.WATERING: [
				"water",
				"watering",
				"how much water",
				"how often",
				"irrigation",
				"daily water",
				"weekly water"
			],

			Intent.FERTILIZER: [
				"fertilizer",
				"fertiliser",
				"npk",
				"compost",
				"manure",
				"nutrients",
				"feed plant"
			],

			Intent.GROWTH_ADVICE: [
				"grow",
				"growth",
				"grow faster",
				"increase growth",
				"boost growth",
				"care tips"
			],

			Intent.PRUNING: [
				"prune",
				"pruning",
				"trim",
				"cut branches",
				"remove leaves"
			],

			Intent.PEST_CONTROL: [
				"pest",
				"insects",
				"bugs",
				"aphids",
				"mites",
				"worms",
				"caterpillar",
				"snails"
			],

			Intent.HARVESTING: [
				"harvest",
				"harvesting",
				"ready to harvest",
				"when to harvest",
				"pick fruit"
			],

			Intent.SOIL_MANAGEMENT: [
				"soil",
				"soil type",
				"soil ph",
				"drainage",
				"potting mix"
			],

			Intent.SUNLIGHT: [
				"sunlight",
				"sun",
				"shade",
				"light requirement",
				"full sun",
				"partial shade"
			],

			Intent.TEMPERATURE: [
				"temperature",
				"cold",
				"heat",
				"hot weather",
				"frost"
			],

			Intent.HUMIDITY: [
				"humidity",
				"moisture",
				"humid"
			],

			Intent.PROPAGATION: [
				"propagation",
				"cutting",
				"seed",
				"grafting",
				"layering"
			],

			Intent.REPOTTING: [
				"repot",
				"repotting",
				"change pot",
				"bigger pot"
			],

			Intent.FLOWERING: [
				"flower",
				"flowering",
				"more flowers",
				"buds"
			],

			Intent.FRUITING: [
				"fruit",
				"fruiting",
				"more fruits",
				"fruit production"
			],

			Intent.SEED_INFORMATION: [
				"seed",
				"germination",
				"germinate",
				"seedlings"
			],

			Intent.NUTRIENT_DEFICIENCY: [
				"nutrient deficiency",
				"nitrogen deficiency",
				"potassium deficiency",
				"phosphorus deficiency",
				"magnesium deficiency",
				"iron deficiency"
			],

			Intent.TOXICITY: [
				"fertilizer burn",
				"chemical damage",
				"toxicity",
				"over fertilized",
				"overwatered"
			],

			Intent.WEED_MANAGEMENT: [
				"weed",
				"weeds",
				"weed control"
			],

			Intent.CROP_RECOMMENDATION: [
				"which crop",
				"crop recommendation",
				"best crop",
				"what should i grow"
			],

			Intent.COMPANION_PLANTING: [
				"companion planting",
				"grow together",
				"compatible plants"
			],

			Intent.SEASONAL_CARE: [
				"summer care",
				"winter care",
				"rainy season",
				"seasonal care"
			],

			Intent.WEATHER_ADVICE: [
				"weather",
				"rain",
				"temperature forecast",
				"climate"
			]
		}

	def detect(self, query: str | None) -> Intent:
		if not query:
			return Intent.GENERAL_QUESTION

		text = query.lower().strip()

		for intent, keywords in self.intent_keywords.items():
			for keyword in keywords:
				if keyword in text:
					return intent

		return Intent.GENERAL_QUESTION