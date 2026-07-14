import { useState } from "react"

import {
	FaCloudRain,
	FaTemperatureHigh,
	FaTint,
	FaWind
} from "react-icons/fa"

function WeatherWidget({
	weather
}) {

	const [open, setOpen] = useState(false)

	if (!weather) {

		return null

	}

	return (

		<div className="fixed right-6 top-6 z-50">

			<button

				onClick={() => setOpen(!open)}

				className="
					flex items-center gap-3
					rounded-full
					bg-white
					px-5
					py-3
					shadow-xl
					transition
					duration-300
					hover:scale-105
				"

			>

				<div className="text-3xl">

					☀️

				</div>

				<div className="text-left">

					<p className="text-2xl font-bold">

						{weather.temperature}°C

					</p>

					<p className="text-sm text-gray-500">

						{weather.wind_speed} km/h

					</p>

				</div>

			</button>

			{

				open && (

					<div
						className="
							mt-3
							w-80
							rounded-3xl
							bg-white
							p-6
							shadow-2xl
						"
					>

						<h2 className="mb-6 text-xl font-bold">

							Today's Weather

						</h2>

						<div className="space-y-4">

							<div className="flex justify-between">

								<span className="flex items-center gap-2">

									<FaTemperatureHigh />

									Temperature

								</span>

								<span>

									{weather.temperature}°C

								</span>

							</div>

							<div className="flex justify-between">

								<span>

									Feels Like

								</span>

								<span>

									{weather.feels_like}°C

								</span>

							</div>

							<div className="flex justify-between">

								<span className="flex items-center gap-2">

									<FaTint />

									Humidity

								</span>

								<span>

									{weather.humidity}%

								</span>

							</div>

							<div className="flex justify-between">

								<span className="flex items-center gap-2">

									<FaWind />

									Wind

								</span>

								<span>

									{weather.wind_speed} km/h

								</span>

							</div>

							<div className="flex justify-between">

								<span className="flex items-center gap-2">

									<FaCloudRain />

									Rain

								</span>

								<span>

									{weather.rain_probability}%

								</span>

							</div>

							<div className="flex justify-between">

								<span>

									Condition

								</span>

								<span>

									{weather.condition}

								</span>

							</div>

						</div>

					</div>

				)

			}

		</div>

	)

}

export default WeatherWidget