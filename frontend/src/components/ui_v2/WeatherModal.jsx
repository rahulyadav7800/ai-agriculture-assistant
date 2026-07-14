import { AnimatePresence, motion } from "framer-motion"

import {
	FaCloud,
	FaMapMarkerAlt,
	FaTemperatureHigh,
	FaTint,
	FaWind,
	FaCloudRain,
	FaTimes
} from "react-icons/fa"

function WeatherModal({

	open,

	onClose,

	weather

}) {

	if (!weather) {

		return null

	}

	const getConditionIcon = () => {

		const condition = (

			weather.condition ||

			weather.weather ||

			""

		).toLowerCase()

		if (condition.includes("rain")) {

			return "🌧"

		}

		if (condition.includes("cloud")) {

			return "☁"

		}

		if (condition.includes("storm")) {

			return "⛈"

		}

		if (condition.includes("fog")) {

			return "🌫"

		}

		return "☀"

	}

	return (

		<AnimatePresence>

			{

				open && (

					<>

						<motion.div

							initial={{
								opacity: 0
							}}

							animate={{
								opacity: 1
							}}

							exit={{
								opacity: 0
							}}

							onClick={onClose}

							className="
								fixed
								inset-0
								z-50
								bg-black/50
								backdrop-blur-sm
							"

						/>

						<motion.div

							initial={{
								opacity: 0,
								scale: 0.9,
								y: 20
							}}

							animate={{
								opacity: 1,
								scale: 1,
								y: 0
							}}

							exit={{
								opacity: 0,
								scale: 0.9,
								y: 20
							}}

							transition={{
								duration: 0.25
							}}

							className="
								fixed
								left-1/2
								top-1/2
								z-[60]
								w-[92%]
								max-w-md
								-translate-x-1/2
								-translate-y-1/2
								overflow-hidden
								rounded-3xl
								border
								border-green-300
								bg-white/90
								p-6
								shadow-2xl
								backdrop-blur-xl

								dark:border-green-500/20
								dark:bg-[#101914]/90
							"

						>

							<div
								className="
									mb-6
									flex
									items-center
									justify-between
								"
							>

								<div>

									<h2
										className="
											text-2xl
											font-bold
											text-gray-800
											dark:text-white
										"
									>

										Weather Details

									</h2>

									<div
										className="
											mt-1
											flex
											items-center
											gap-2
											text-sm
											text-gray-500
											dark:text-gray-400
										"
									>

										<FaMapMarkerAlt />

										<span>

											{weather.city}

										</span>

									</div>

								</div>

								<button

									onClick={onClose}

									className="
										rounded-full
										p-2
										text-gray-500
										transition
										hover:bg-gray-100

										dark:text-gray-300
										dark:hover:bg-white/10
									"

								>

									<FaTimes />

								</button>

							</div>

							<div
								className="
									mb-6
									text-center
								"
							>

								<div className="text-6xl">

									{getConditionIcon()}

								</div>

								<h3
									className="
										mt-3
										text-4xl
										font-bold
										text-green-600
										dark:text-green-400
									"
								>

									{weather.temperature}°C

								</h3>

								<p
									className="
										mt-2
										text-gray-500
										dark:text-gray-400
									"
								>

									{weather.condition || "Current Weather"}

								</p>

							</div>

							<div className="grid gap-4 sm:grid-cols-2">

								<div className="rounded-2xl bg-green-50 p-4 dark:bg-green-500/10">

									<div className="flex items-center gap-3">

										<FaTemperatureHigh className="text-green-600 dark:text-green-400" />

										<div>

											<p className="text-sm text-gray-500 dark:text-gray-400">

												Feels Like

											</p>

											<p className="font-semibold text-gray-800 dark:text-white">

												{weather.feels_like ?? "--"}°C

											</p>

										</div>

									</div>

								</div>

								<div className="rounded-2xl bg-green-50 p-4 dark:bg-green-500/10">

									<div className="flex items-center gap-3">

										<FaTint className="text-blue-500" />

										<div>

											<p className="text-sm text-gray-500 dark:text-gray-400">

												Humidity

											</p>

											<p className="font-semibold text-gray-800 dark:text-white">

												{weather.humidity ?? "--"}%

											</p>

										</div>

									</div>

								</div>

								<div className="rounded-2xl bg-green-50 p-4 dark:bg-green-500/10">

									<div className="flex items-center gap-3">

										<FaWind className="text-cyan-500" />

										<div>

											<p className="text-sm text-gray-500 dark:text-gray-400">

												Wind

											</p>

											<p className="font-semibold text-gray-800 dark:text-white">

												{weather.wind_speed ?? "--"} km/h

											</p>

										</div>

									</div>

								</div>

								<div className="rounded-2xl bg-green-50 p-4 dark:bg-green-500/10">

									<div className="flex items-center gap-3">

										<FaCloudRain className="text-sky-500" />

										<div>

											<p className="text-sm text-gray-500 dark:text-gray-400">

												Rain

											</p>

											<p className="font-semibold text-gray-800 dark:text-white">

												{weather.rain_probability ?? 0} %

											</p>

										</div>

									</div>

								</div>

							</div>

						</motion.div>

					</>

				)

			}

		</AnimatePresence>

	)

}

export default WeatherModal