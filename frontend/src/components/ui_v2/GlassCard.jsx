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
				bg-white/80
				backdrop-blur-xl
				p-6
				shadow-xl
				transition-all
				duration-300
				hover:-translate-y-1
				hover:shadow-2xl
				${className}
			`}

		>

			{children}

		</div>

	)

}

export default GlassCard