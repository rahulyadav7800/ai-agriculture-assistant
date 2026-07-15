import { useState } from "react"

import useWeather from "../../hooks/useWeather"

import { useTheme } from "../../context/ThemeContext"

import WeatherModal from "../ui_v2/WeatherModal"

import {
	FaLeaf,
	FaCircle,
	FaMoon,
	FaSun
} from "react-icons/fa"

function Navbar() {

	const { weather } = useWeather()

	const [openWeather, setOpenWeather] = useState(false)

	const {
		theme,
		toggleTheme
	} = useTheme()

	return (

		<>

			<header
				className="
					sticky
					top-0
					z-50
					border-b
					border-green-200/60
					bg-white/60
					backdrop-blur-2xl
					shadow-lg
					shadow-black/5
					transition-all
					duration-300

					dark:border-green-500/20
					dark:bg-[#08120d]/45
					dark:shadow-black/30
				"
			>

				<div
	className="
		mx-auto
		flex
		max-w-7xl
		flex-wrap
		items-center
		justify-between
		gap-4
		px-4
		py-4
	"
>

					<div
	className="
		flex
		flex-wrap
		items-center
		justify-end
		gap-2
	"
>

						<div
							className="
								flex
								h-12
								w-12
								items-center
								justify-center
								rounded-2xl
								bg-gradient-to-br
								from-green-500
								to-emerald-400
								text-xl
								text-white
								shadow-lg
								shadow-green-500/30
							"
						>

							<FaLeaf />

						</div>

						<div>

							<h1
								className="
									text-2xl
									font-bold
									text-gray-900
									transition-colors
									duration-300
									dark:text-white
								"
							>

								AI Agriculture Assistant

							</h1>

							<p
								className="
									text-sm
									text-gray-500
									transition-colors
									duration-300
									dark:text-gray-400
								"
							>

								AI-Powered Plant Intelligence

							</p>

						</div>

					</div>

					<div
						className="
							flex
							items-center
							gap-4
						"
					>

						{

							weather && (

								<button

									onClick={() =>

										setOpenWeather(true)

									}

									className="
	flex
	items-center
	gap-2
	rounded-full
	border
	border-green-200
	bg-green-50/70
	px-3
	py-2
	text-xs
	font-medium
	text-green-700
	backdrop-blur-md
	transition-all
	duration-300

	dark:border-green-500/20
	dark:bg-green-500/10
	dark:text-green-300
"

								>

									<span>

										☀ {weather.temperature}°C

									</span>

									<span>

										🌬 {weather.wind_speed} km/h

									</span>

								</button>

							)

						}

						<button

							onClick={toggleTheme}

							className="
								flex
								h-11
								w-11
								items-center
								justify-center
								rounded-full
								border
								border-green-200
								bg-white/70
								text-green-700
								backdrop-blur-md
								transition-all
								duration-300
								hover:scale-110
								hover:rotate-12
								hover:border-green-400
								hover:bg-green-100

								dark:border-green-500/20
								dark:bg-green-500/10
								dark:text-yellow-300
								dark:hover:bg-green-500/20
							"

							title="Toggle Theme"

						>

							{

								theme === "light"

									? <FaMoon />

									: <FaSun />

							}

						</button>

						<div
							className="
								hidden
								items-center
								gap-2
								lg:flex
							"
						>

							<FaCircle
								className="
									text-[10px]
									text-green-500
								"
							/>

							<span
								className="
									text-sm
									font-medium
									text-gray-600
									transition-colors
									duration-300
									dark:text-gray-300
								"
							>

								System Online

							</span>

						</div>

					</div>

				</div>

			</header>

			<WeatherModal

				open={openWeather}

				onClose={() =>

					setOpenWeather(false)

				}

				weather={weather}

			/>

		</>

	)

}

export default Navbar