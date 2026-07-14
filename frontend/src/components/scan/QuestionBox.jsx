function QuestionBox({
	question,
	setQuestion
}) {

	return (

		<div className="rounded-xl bg-white p-6 shadow-lg">

			<h2 className="mb-4 text-2xl font-bold text-green-700">

				💬 Ask Your Question

			</h2>

			<textarea
				rows={4}
				value={question}
				onChange={(event) => setQuestion(event.target.value)}
				placeholder="Example: Why are the leaves turning yellow?"
				className="w-full rounded-lg border border-gray-300 p-4 outline-none focus:border-green-600"
			/>

		</div>

	)

}

export default QuestionBox