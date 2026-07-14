import useWeather from "../../hooks/useWeather"

import { WiHumidity } from "react-icons/wi"
import { FaTemperatureHigh } from "react-icons/fa"
import { MdAir } from "react-icons/md"
import { BsCloudRainHeavyFill } from "react-icons/bs"
import { IoCloudOutline } from "react-icons/io5"



function WeatherCard() {

	const { weather, loading, error } = useWeather()

	if (loading) {

		return (

			<div className="rounded-xl bg-white p-6 shadow">

				Loading weather...

			</div>

		)

	}

	if (error) {

		return (

			<div className="rounded-xl bg-red-100 p-6 text-red-700 shadow">

				{error}

			</div>

		)

	}

	return (

		<div className="rounded-xl bg-white p-6 shadow-lg">

			<h2 className="mb-6 text-2xl font-bold text-green-700">

				🌤 Current Weather

			</h2>

			<div className="grid grid-cols-2 gap-6">

				<div className="flex items-center gap-3">

					<FaTemperatureHigh
						size={24}
					/>

					<div>

						<p className="text-sm text-gray-500">

							Temperature

						</p>

						<p className="font-semibold">

							{weather.temperature} °C

						</p>

					</div>

				</div>

				<div className="flex items-center gap-3">

					<FaTemperatureHigh
						size={24}
					/>

					<div>

						<p className="text-sm text-gray-500">

							Feels Like

						</p>

						<p className="font-semibold">

							{weather.feels_like} °C

						</p>

					</div>

				</div>

				<div className="flex items-center gap-3">

					<WiHumidity
						size={32}
					/>

					<div>

						<p className="text-sm text-gray-500">

							Humidity

						</p>

						<p className="font-semibold">

							{weather.humidity} %

						</p>

					</div>

				</div>

				<div className="flex items-center gap-3">

					<MdAir
						size={24}
					/>

					<div>

						<p className="text-sm text-gray-500">

							Wind

						</p>

						<p className="font-semibold">

							{weather.wind_speed} km/h

						</p>

					</div>

				</div>

				<div className="flex items-center gap-3">

					<BsCloudRainHeavyFill
						size={22}
					/>

					<div>

						<p className="text-sm text-gray-500">

							Rain

						</p>

						<p className="font-semibold">

							{weather.rain_probability} %

						</p>

					</div>

				</div>

				<div className="flex items-center gap-3">

					<IoCloudOutline
						size={24}
					/>

					<div>

						<p className="text-sm text-gray-500">

							Condition

						</p>

						<p className="font-semibold">

							{weather.condition}

						</p>

					</div>

				</div>

			</div>

		</div>

	)

}

export default WeatherCard