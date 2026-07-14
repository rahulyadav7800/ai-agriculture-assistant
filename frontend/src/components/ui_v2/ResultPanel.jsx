import { useEffect, useMemo, useState } from "react"

import { motion } from "framer-motion"

import GlassCard from "./GlassCard"

function ResultPanel({

	result,

	selectedFile

}) {

	const [animatedConfidence, setAnimatedConfidence] = useState(0)

	const previewUrl = useMemo(() => {

		if (!selectedFile) {

			return null

		}

		return URL.createObjectURL(selectedFile)

	}, [selectedFile])

	useEffect(() => {

		return () => {

			if (previewUrl) {

				URL.revokeObjectURL(previewUrl)

			}

		}

	}, [previewUrl])

	useEffect(() => {

		if (!result) {

			return

		}

		const target = Math.round(

			Number(result.plant.confidence)

		)

		let value = 0

		const interval = setInterval(() => {

			value += 1

			if (value >= target) {

				value = target

				clearInterval(interval)

			}

			setAnimatedConfidence(value)

		}, 12)

		return () => clearInterval(interval)

	}, [result])

	if (!result) {

		return null

	}

	return (

		<motion.div

			initial={{
				opacity: 0,
				y: 40
			}}

			animate={{
				opacity: 1,
				y: 0
			}}

			transition={{
				duration: 0.6
			}}

			className="
				mt-10
				grid
				gap-6
				lg:grid-cols-3
			"

		>

			<motion.div

				initial={{
					opacity: 0,
					x: -25
				}}

				animate={{
					opacity: 1,
					x: 0
				}}

				transition={{
					delay: 0.15
				}}

			>

				<GlassCard className="overflow-hidden">

					<div
						className="
							group
							overflow-hidden
							rounded-2xl
						"
					>

						<img

							src={previewUrl}

							alt="Plant"

							className="
								h-72
								w-full
								object-cover
								transition-transform
								duration-500
								group-hover:scale-105
							"

						/>

					</div>

					<div className="mt-5 space-y-4">

						<div>

							<p
								className="
									text-sm
									text-gray-500
									transition-colors
									duration-300
									dark:text-gray-400
								"
							>

								Plant Name

							</p>

							<h2
								className="
									mt-1
									text-2xl
									font-bold
									text-gray-800
									transition-colors
									duration-300
									dark:text-white
								"
							>

								{result.plant.plant_name}

							</h2>

						</div>

						<div>

							<p
								className="
									text-sm
									text-gray-500
									transition-colors
									duration-300
									dark:text-gray-400
								"
							>

								Scientific Name

							</p>

							<p
								className="
									mt-1
									italic
									text-gray-700
									transition-colors
									duration-300
									dark:text-gray-300
								"
							>

								{result.plant.scientific_name}

							</p>

						</div>

						<div>

							<p
								className="
									text-sm
									text-gray-500
									transition-colors
									duration-300
									dark:text-gray-400
								"
							>

								Family

							</p>

							<p
								className="
									mt-1
									font-medium
									text-gray-700
									transition-colors
									duration-300
									dark:text-gray-200
								"
							>

								{result.plant.family}

							</p>

						</div>

						<div>

							<div
								className="
									mb-2
									flex
									items-center
									justify-between
								"
							>

								<span
									className="
										font-medium
										text-gray-800
										transition-colors
										duration-300
										dark:text-gray-100
									"
								>

									Confidence

								</span>

								<span
									className="
										font-bold
										text-green-700
										transition-colors
										duration-300
										dark:text-green-400
									"
								>

									{animatedConfidence}%

								</span>

							</div>

							<div
								className="
									h-3
									w-full
									overflow-hidden
									rounded-full
									bg-green-100
									dark:bg-green-900/40
								"
							>

								<motion.div

									initial={{
										width: 0
									}}

									animate={{
										width: `${animatedConfidence}%`
									}}

									transition={{
										duration: 0.8
									}}

									className="
										h-full
										rounded-full
										bg-gradient-to-r
										from-green-500
										to-emerald-400
									"

								/>

							</div>

						</div>
                        					</div>

				</GlassCard>

			</motion.div>

			<motion.div

				className="lg:col-span-2"

				initial={{
					opacity: 0,
					x: 25
				}}

				animate={{
					opacity: 1,
					x: 0
				}}

				transition={{
					delay: 0.3
				}}

			>

				<GlassCard
					className="
						h-full
						hover:shadow-green-500/10
					"
				>

					<h2
						className="
							mb-4
							text-3xl
							font-bold
							text-gray-800
							transition-colors
							duration-300
							dark:text-white
						"
					>

						🤖 AI Analysis

					</h2>

					<motion.div

						initial={{
							opacity: 0
						}}

						animate={{
							opacity: 1
						}}

						transition={{
							delay: 0.5,
							duration: 0.6
						}}

						className="
							whitespace-pre-wrap
							text-[17px]
							leading-8
							text-gray-700
							transition-colors
							duration-300
							dark:text-gray-200
						"

					>

						{result.diagnosis.answer}

					</motion.div>

				</GlassCard>

			</motion.div>

		</motion.div>

	)

}

export default ResultPanel