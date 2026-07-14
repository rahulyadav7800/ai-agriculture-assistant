import GlassCard from "./GlassCard"

function ResultPanel({

	result,

	selectedFile

}) {

	if (!result) {

		return null

	}

	return (

		<div
			className="
				mt-10
				grid
				gap-6
				lg:grid-cols-2
			"
		>

			<GlassCard>

				<h2
					className="
						mb-6
						text-2xl
						font-bold
						text-gray-800
					"
				>

					🌿 Plant Information

				</h2>

				{

					selectedFile && (

						<img

							src={URL.createObjectURL(selectedFile)}

							alt="Plant"

							className="
								mb-6
								h-64
								w-full
								rounded-2xl
								object-cover
							"

						/>

					)

				}

				<div className="space-y-4">

					<div>

						<p className="text-gray-500">

							Plant Name

						</p>

						<p className="text-xl font-bold">

							{result.plant.plant_name}

						</p>

					</div>

					<div>

						<p className="text-gray-500">

							Scientific Name

						</p>

						<p>

							{result.plant.scientific_name}

						</p>

					</div>

					<div>

						<p className="text-gray-500">

							Family

						</p>

						<p>

							{result.plant.family}

						</p>

					</div>

					<div>

						<p className="text-gray-500">

							Confidence

						</p>

						<p className="font-bold text-green-600">

							{result.plant.confidence}%

						</p>

					</div>

				</div>

			</GlassCard>

			<GlassCard>

				<h2
					className="
						mb-6
						text-2xl
						font-bold
						text-gray-800
					"
				>

					🤖 AI Recommendation

				</h2>

				<div
					className="
						whitespace-pre-wrap
						leading-8
						text-gray-700
					"
				>

					{result.diagnosis.answer}

				</div>

			</GlassCard>

		</div>

	)

}

export default ResultPanel