import { motion } from "framer-motion"

function GlowButton({

	children,

	onClick,

	loading = false,

	className = ""

}) {

	return (

		<motion.button

			whileHover={{
				scale: 1.03
			}}

			whileTap={{
				scale: 0.97
			}}

			onClick={onClick}

			disabled={loading}

			className={`
				group
				relative
				w-full
				overflow-hidden
				rounded-2xl

				bg-gradient-to-r
				from-green-500
				via-emerald-500
				to-green-400

				px-8
				py-4

				text-lg
				font-semibold
				text-white

				shadow-lg
				shadow-green-500/30

				transition-all
				duration-300

				hover:shadow-2xl
				hover:shadow-green-500/40

				active:scale-[0.98]

				disabled:cursor-not-allowed
				disabled:opacity-70

				dark:shadow-green-500/20
				dark:hover:shadow-green-400/50

				${className}
			`}

		>

			<div
				className="
					absolute
					inset-0
					bg-white/10
					opacity-0
					transition-opacity
					duration-300
					group-hover:opacity-100
				"
			/>

			<span
				className="
					relative
					z-10
					flex
					items-center
					justify-center
					gap-2
				"
			>

				{

					loading ? (

						<>

							<motion.span

								animate={{
									rotate: 360
								}}

								transition={{
									repeat: Infinity,
									duration: 1,
									ease: "linear"
								}}

							>

								🌿

							</motion.span>

							Analyzing...

						</>

					) : (

						children

					)

				}

			</span>

		</motion.button>

	)

}

export default GlowButton