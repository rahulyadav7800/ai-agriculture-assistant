function ResponseCard({
	diagnosis
}) {

	if (!diagnosis) {

		return null

	}

	return (

		<div className="rounded-xl bg-white p-6 shadow-lg">

			<h2 className="mb-6 text-2xl font-bold text-green-700">

				🤖 AI Analysis

			</h2>

			<p className="whitespace-pre-line leading-8 text-gray-700">

				{diagnosis.answer}

			</p>

		</div>

	)

}

export default ResponseCard
