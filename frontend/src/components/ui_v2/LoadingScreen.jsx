import { useEffect, useState } from "react"

import { AnimatePresence, motion } from "framer-motion"

import GlassCard from "./GlassCard"

const STAGES = [

	{
		icon: "📤",
		title: "Uploading Image...",
		description: "Preparing your plant image for analysis."
	},

	{
		icon: "🌿",
		title: "Identifying Plant...",
		description: "Matching your plant with the PlantNet database."
	},

	{
		icon: "👁️",
		title: "Vision Analysis...",
		description: "Inspecting leaves, stems and visible symptoms."
	},

	{
		icon: "🤖",
		title: "Generating Recommendation...",
		description: "AI is preparing diagnosis and treatment."
	},

	{
		icon: "🌦️",
		title: "Fetching Weather...",
		description: "Collecting local weather information."
	},

	{
		icon: "✅",
		title: "Almost Done...",
		description: "Preparing your final report."
	}

]

function LoadingScreen() {

	const [stage, setStage] = useState(0)

	useEffect(() => {

		const interval = setInterval(() => {

			setStage((current) => {

				if (current >= STAGES.length - 1) {

					return current

				}

				return current + 1

			})

		}, 3500)

		return () => clearInterval(interval)

	}, [])

	const progress = ((stage + 1) / STAGES.length) * 100

	return (

		<GlassCard className="mt-10">

			<div
				className="
					flex
					flex-col
					items-center
					py-8
					text-center
				"
			>

				<motion.div

					animate={{
						scale: [1, 1.15, 1],
						rotate: [0, 5, -5, 0]
					}}

					transition={{
						duration: 2,
						repeat: Infinity
					}}

					className="text-7xl"

				>

					{STAGES[stage].icon}

				</motion.div>

				<AnimatePresence mode="wait">

					<motion.div

						key={stage}

						initial={{
							opacity: 0,
							y: 15
						}}

						animate={{
							opacity: 1,
							y: 0
						}}

						exit={{
							opacity: 0,
							y: -15
						}}

						transition={{
							duration: 0.35
						}}

						className="mt-8"

					>

						<h2
							className="
								text-3xl
								font-bold
								text-gray-800
							"
						>

							{STAGES[stage].title}

						</h2>

						<p
							className="
								mt-3
								max-w-xl
								text-gray-500
							"
						>

							{STAGES[stage].description}

						</p>

					</motion.div>

				</AnimatePresence>

				<div
					className="
						mt-10
						h-4
						w-full
						max-w-2xl
						overflow-hidden
						rounded-full
						bg-gray-200
					"
				>

					<motion.div

						animate={{
							width: `${progress}%`
						}}

						transition={{
							duration: 0.6
						}}

						className="
							h-full
							rounded-full
							bg-gradient-to-r
							from-green-500
							via-emerald-400
							to-lime-400
						"

					/>

				</div>

				<div
					className="
						mt-4
						text-lg
						font-semibold
						text-green-700
					"
				>

					{Math.round(progress)}%

				</div>

				<p
					className="
						mt-8
						text-gray-500
					"
				>

					This usually takes around 20-30 seconds.

				</p>

</div>

		</GlassCard>

	)

}

export default LoadingScreen