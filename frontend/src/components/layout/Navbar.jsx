import useWeather from "../../hooks/useWeather"

import {
	FaLeaf,
	FaCircle
} from "react-icons/fa"

function Navbar() {

	const { weather } = useWeather()

	return (

		<header
			className="
				sticky
				top-0
				z-50
				border-b
				border-green-100
				bg-white/80
				backdrop-blur-xl
				shadow-sm
			"
		>

			<div
				className="
					mx-auto
					flex
					max-w-7xl
					items-center
					justify-between
					px-6
					py-4
				"
			>

				<div className="flex items-center gap-4">

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
							"
						>

							AI Agriculture Assistant

						</h1>

						<p
							className="
								text-sm
								text-gray-500
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

							<div
								className="
									flex
                                    rounded-full
                                    bg-green-50
                                    px-3
                                    py-2
                                    text-xs
                                    font-medium
                                    text-green-700
                                    items-center
                                    gap-2
                                    sm:px-4
                                    sm:text-sm
                                    sm:gap-4
								"
							>

								<span>

									☀ {weather.temperature}°C

								</span>

								<span>

									🌬 {weather.wind_speed} km/h

								</span>

							</div>

						)
					}

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
							"
						>

							System Online

						</span>

					</div>

				</div>

			</div>

		</header>

	)

}

export default Navbar