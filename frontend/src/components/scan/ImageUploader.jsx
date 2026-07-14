import { useRef } from "react"

function ImageUploader({
	selectedFile,
	setSelectedFile
}) {

	const inputRef = useRef(null)

	const handleImageChange = (event) => {

		const file = event.target.files[0]

		if (!file) {

			return

		}

		setSelectedFile(file)

	}

	return (

		<div className="rounded-xl bg-white p-6 shadow-lg">

			<h2 className="mb-4 text-2xl font-bold text-green-700">

				📷 Upload Plant Image

			</h2>

			<input
				ref={inputRef}
				type="file"
				accept="image/*"
				className="hidden"
				onChange={handleImageChange}
			/>

			<button
				type="button"
				onClick={() => inputRef.current.click()}
				className="rounded-lg bg-green-700 px-6 py-3 font-semibold text-white transition hover:bg-green-800"
			>

				Choose Image

			</button>

			{
				selectedFile && (

					<div className="mt-6">

						<img
							src={URL.createObjectURL(selectedFile)}
							alt="Selected Plant"
							className="mx-auto max-h-80 rounded-lg border shadow"
						/>

					</div>

				)
			}

		</div>

	)

}

export default ImageUploader