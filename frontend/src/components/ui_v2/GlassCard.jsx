function GlassCard({

	children,

	className = ""

}) {

	return (

		<div

			className={`
				rounded-3xl

				border
				border-green-500/20

				bg-white/75

				backdrop-blur-2xl

				p-6

				shadow-xl
				shadow-black/5

				transition-all
				duration-300

				hover:-translate-y-0.5
				hover:shadow-2xl
				hover:shadow-green-500/10

				dark:border-green-500/20

				dark:bg-white/5

				dark:shadow-black/30

				dark:hover:border-green-400/30
				dark:hover:shadow-green-500/20

				${className}
			`}

		>

			{children}

		</div>

	)

}

export default GlassCard