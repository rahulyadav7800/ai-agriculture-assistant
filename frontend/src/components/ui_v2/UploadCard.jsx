import { useMemo, useRef } from "react"

import { FaCloudUploadAlt } from "react-icons/fa"

import GlassCard from "./GlassCard"
import GlowButton from "./GlowButton"

function UploadCard({

	selectedFile,

	setSelectedFile

}) {

	const fileInputRef = useRef(null)

	const previewUrl = useMemo(() => {

		if (!selectedFile) {

			return null

		}

		return URL.createObjectURL(selectedFile)

	}, [selectedFile])

	const handleBrowse = () => {

		fileInputRef.current.click()

	}

	const handleFileChange = (event) => {

		const file = event.target.files[0]

		if (!file) {

			return

		}

		setSelectedFile(file)

	}

	return (

		<GlassCard>

			<input

				ref={fileInputRef}

				type="file"

				accept="image/*"

				className="hidden"

				onChange={handleFileChange}

			/>

			{

				selectedFile ? (

					<div
						className="
							flex
							flex-col
							items-center
							rounded-2xl
							border-2
							border-green-300
							bg-green-50
							p-8
						"
					>

						<img

							src={previewUrl}

							alt="Preview"

							className="
								h-72
								w-full
								rounded-xl
								object-cover
								shadow-lg
							"

						/>

						<h3
							className="
								mt-6
								text-xl
								font-bold
								text-gray-800
							"
						>

							{selectedFile.name}

						</h3>

						<p
							className="
								mt-2
								font-medium
								text-green-600
							"
						>

							✅ Ready to Analyze

						</p>

						<div
							className="
								mt-6
								w-56
							"
						>

							<GlowButton
								onClick={handleBrowse}
							>

								Change Image

							</GlowButton>

						</div>

					</div>

				) : (

					<div
						className="
							flex
							flex-col
							items-center
							justify-center
							rounded-2xl
							border-2
							border-dashed
							border-green-300
							bg-green-50
							p-12
							text-center
							transition
							duration-300
							hover:border-green-500
							hover:bg-green-100
						"
					>

						<FaCloudUploadAlt
							className="
								mb-6
								text-7xl
								text-green-600
							"
						/>

						<h2
							className="
								text-2xl
								font-bold
								text-gray-800
							"
						>

							Upload Plant Image

						</h2>

						<p
							className="
								mt-3
								text-gray-500
							"
						>

							Drag & Drop your image here

						</p>

						<p
							className="
								my-4
								text-gray-400
							"
						>

							or

						</p>

						<div className="w-56">

							<GlowButton
								onClick={handleBrowse}
							>

								Browse Files

							</GlowButton>

						</div>

						<p
							className="
								mt-6
								text-sm
								text-gray-400
							"
						>

							JPG • JPEG • PNG • WEBP

						</p>

					</div>

				)

			}

		</GlassCard>

	)

}

export default UploadCard