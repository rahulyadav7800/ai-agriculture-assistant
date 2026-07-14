function PlantCard({
	plant
}) {

	if (!plant) {

		return null

	}

	return (

		<div className="rounded-xl bg-white p-6 shadow-lg">

			<h2 className="mb-6 text-2xl font-bold text-green-700">

				🌿 Plant Information

			</h2>

			<div className="space-y-4">

				<div className="flex justify-between border-b pb-2">

					<span className="font-medium text-gray-600">

						Plant Name

					</span>

					<span className="font-semibold">

						{plant.plant_name}

					</span>

				</div>

				<div className="flex justify-between border-b pb-2">

					<span className="font-medium text-gray-600">

						Scientific Name

					</span>

					<span className="font-semibold italic">

						{plant.scientific_name}

					</span>

				</div>

				<div className="flex justify-between border-b pb-2">

					<span className="font-medium text-gray-600">

						Family

					</span>

					<span className="font-semibold">

						{plant.family}

					</span>

				</div>

				<div className="flex justify-between">

					<span className="font-medium text-gray-600">

						Confidence

					</span>

					<span className="font-bold text-green-700">

						{plant.confidence}%

					</span>

				</div>

			</div>

		</div>

	)

}

export default PlantCard