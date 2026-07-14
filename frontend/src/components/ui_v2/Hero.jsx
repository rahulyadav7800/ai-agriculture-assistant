import { motion } from "framer-motion"

import {
	FaLeaf,
	FaSeedling,
	FaRobot,
	FaBug
} from "react-icons/fa"

function Hero() {

	const features = [

		{
			icon: <FaLeaf />,
			text: "Plant Identification"
		},

		{
			icon: <FaBug />,
			text: "Disease Detection"
		},

		{
			icon: <FaRobot />,
			text: "AI Recommendations"
		},

		{
			icon: <FaSeedling />,
			text: "Plant Care"
		}

	]

	return (

		<section className="py-14">

			<motion.div

				initial={{
					opacity: 0,
					y: -30
				}}

				animate={{
					opacity: 1,
					y: 0
				}}

				transition={{
					duration: .7
				}}

				className="mx-auto max-w-5xl text-center"

			>

				<div className="mb-6 flex justify-center">

					<div
						className="
							flex
							h-24
							w-24
							items-center
							justify-center
							rounded-full
							bg-gradient-to-br
							from-green-500
							to-emerald-400
							text-5xl
							text-white
							shadow-2xl
							shadow-green-500/40
						"
					>

						<FaLeaf />

					</div>

				</div>

				<h1
					className="
						text-5xl
						font-black
						text-gray-900
						lg:text-6xl
					"
				>

					AI Agriculture Assistant

				</h1>

				<p
					className="
						mx-auto
						mt-6
						max-w-3xl
						text-lg
						leading-8
						text-gray-600
					"
				>

					Upload a plant photo and receive
					AI-powered plant identification,
					disease analysis and personalized
					care recommendations within seconds.

				</p>

				<div
					className="
						mt-10
						flex
						flex-wrap
						justify-center
						gap-4
					"
				>

					{

						features.map(

							(feature) => (

								<motion.div

									key={feature.text}

									whileHover={{
										scale: 1.05
									}}

									className="
										flex
										items-center
										gap-2
										rounded-full
										bg-green-100
										px-5
										py-3
										text-green-700
										shadow-md
									"

								>

									<span
										className="text-lg"
									>

										{feature.icon}

									</span>

									<span>

										{feature.text}

									</span>

								</motion.div>

							)

						)

					}

				</div>

			</motion.div>

		</section>

	)

}

export default Hero