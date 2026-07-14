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
				w-full
				rounded-2xl
				bg-gradient-to-r
				from-green-500
				to-emerald-400
				px-8
				py-4
				text-lg
				font-semibold
				text-white
				shadow-lg
				shadow-green-500/30
				transition-all
				duration-300
				hover:shadow-green-400/60
				disabled:cursor-not-allowed
				disabled:opacity-70
				${className}
			`}

		>

			{

				loading

					? "Analyzing..."

					: children

			}

		</motion.button>

	)

}

export default GlowButton