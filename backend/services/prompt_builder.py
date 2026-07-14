from backend.services.intent_detector import Intent


class PromptBuilder:
	"""
	Builds the final prompt for the LLM based on
	the detected user intent.
	"""

	def __init__(self):
		self.system_prompt = """
You are an expert AI Agriculture Assistant.

Your responsibilities:

1. Answer only plant and agriculture related questions.
2. Use PlantNet result as plant identification.
3. Use Vision Analysis as the primary source for visual understanding.
4. Never guess information that is not supported by the provided data.
5. If information is uncertain, clearly mention it.
6. Return ONLY valid JSON.
7. Do not include markdown.
8. Do not explain the JSON.
"""

		self.intent_prompts = {

			Intent.PLANT_IDENTIFICATION: """
Identify the plant using PlantNet and Vision Analysis.

Return JSON:

{
	"type":"plant_identification",
	"plant_name":"",
	"scientific_name":"",
	"family":"",
	"confidence":0,
	"description":""
}
""",

			Intent.DISEASE_DIAGNOSIS: """
Analyze the plant for diseases.

Use Vision Analysis as the primary evidence.

Return JSON:

{
	"type":"disease_diagnosis",
	"disease":"",
	"confidence":0,
	"possible_causes":[],
	"symptoms":[],
	"treatment":[]
}
""",

			Intent.PLANT_HEALTH: """
Evaluate the overall health of the plant.

Return JSON:

{
	"type":"plant_health",
	"health_status":"",
	"confidence":0,
	"issues":[],
	"recommendations":[]
}
""",

			Intent.WATERING: """
Provide watering recommendations.

Return JSON:

{
	"type":"watering",
	"watering":"",
	"frequency":"",
	"tips":[]
}
""",

			Intent.FERTILIZER: """
Recommend fertilizers.

Return JSON:

{
	"type":"fertilizer",
	"recommended_fertilizers":[],
	"application":"",
	"frequency":""
}
""",

			Intent.GROWTH_ADVICE: """
Provide plant growth recommendations.

Return JSON:

{
	"type":"growth_advice",
	"sunlight":"",
	"soil":"",
	"watering":"",
	"fertilizer":"",
	"tips":[]
}
""",

			Intent.PRUNING: """
Provide pruning advice.

Return JSON:

{
	"type":"pruning",
	"best_time":"",
	"steps":[],
	"tips":[]
}
""",

			Intent.PEST_CONTROL: """
Identify pests and provide treatment.

Return JSON:

{
	"type":"pest_control",
	"pests":[],
	"organic_control":[],
	"chemical_control":[]
}
""",

			Intent.HARVESTING: """
Provide harvesting advice.

Return JSON:

{
	"type":"harvesting",
	"ready":"",
	"best_time":"",
	"tips":[]
}
""",

			Intent.SOIL_MANAGEMENT: """
Provide soil recommendations.

Return JSON:

{
	"type":"soil_management",
	"soil_type":"",
	"ph":"",
	"drainage":"",
	"tips":[]
}
""",

			Intent.SUNLIGHT: """
Provide sunlight recommendations.

Return JSON:

{
	"type":"sunlight",
	"requirement":"",
	"daily_hours":"",
	"tips":[]
}
""",

			Intent.TEMPERATURE: """
Provide temperature recommendations.

Return JSON:

{
	"type":"temperature",
	"ideal_range":"",
	"minimum":"",
	"maximum":""
}
""",

			Intent.HUMIDITY: """
Provide humidity recommendations.

Return JSON:

{
	"type":"humidity",
	"ideal_humidity":"",
	"tips":[]
}
""",

			Intent.PROPAGATION: """
Explain plant propagation.

Return JSON:

{
	"type":"propagation",
	"methods":[],
	"best_method":"",
	"steps":[]
}
""",

			Intent.REPOTTING: """
Provide repotting advice.

Return JSON:

{
	"type":"repotting",
	"when":"",
	"pot_size":"",
	"steps":[]
}
""",

			Intent.FLOWERING: """
Provide flowering advice.

Return JSON:

{
	"type":"flowering",
	"status":"",
	"recommendations":[]
}
""",

			Intent.FRUITING: """
Provide fruiting advice.

Return JSON:

{
	"type":"fruiting",
	"status":"",
	"recommendations":[]
}
""",

			Intent.SEED_INFORMATION: """
Provide seed information.

Return JSON:

{
	"type":"seed_information",
	"germination_time":"",
	"planting_depth":"",
	"tips":[]
}
""",

			Intent.NUTRIENT_DEFICIENCY: """
Analyze nutrient deficiencies.

Return JSON:

{
	"type":"nutrient_deficiency",
	"deficiency":"",
	"confidence":0,
	"solution":[]
}
""",

			Intent.TOXICITY: """
Analyze possible toxicity.

Return JSON:

{
	"type":"toxicity",
	"cause":"",
	"severity":"",
	"recommendations":[]
}
""",

			Intent.WEED_MANAGEMENT: """
Provide weed management advice.

Return JSON:

{
	"type":"weed_management",
	"weed_type":"",
	"control_methods":[]
}
""",

			Intent.CROP_RECOMMENDATION: """
Recommend suitable crops.

Return JSON:

{
	"type":"crop_recommendation",
	"recommended_crops":[],
	"reason":""
}
""",

			Intent.COMPANION_PLANTING: """
Recommend companion plants.

Return JSON:

{
	"type":"companion_planting",
	"recommended_plants":[],
	"avoid_plants":[]
}
""",

			Intent.SEASONAL_CARE: """
Provide seasonal care recommendations.

Return JSON:

{
	"type":"seasonal_care",
	"season":"",
	"recommendations":[]
}
""",

			Intent.WEATHER_ADVICE: """
Provide weather-based recommendations.

Return JSON:

{
	"type":"weather_advice",
	"recommendations":[]
}
""",

			Intent.GENERAL_QUESTION: """
Answer the user's plant-related question.

Return JSON:

{
	"type":"general_question",
	"answer":""
}
"""
		}

	def build(
		self,
		intent: Intent,
		user_question: str,
		plantnet_result: str,
		vision_result: str
	) -> str:

		intent_prompt = self.intent_prompts.get(
			intent,
			self.intent_prompts[Intent.GENERAL_QUESTION]
		)

		return f"""
{self.system_prompt}

{intent_prompt}

PlantNet Result:
{plantnet_result}

Vision Analysis:
{vision_result}

User Question:
{user_question}
"""