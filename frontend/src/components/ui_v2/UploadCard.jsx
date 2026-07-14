import { useEffect, useMemo, useRef, useState } from "react"

import { AnimatePresence, motion } from "framer-motion"

import {
	FaCheckCircle,
	FaCloudUploadAlt,
	FaExclamationTriangle,
	FaTrash
} from "react-icons/fa"

import GlassCard from "./GlassCard"
import GlowButton from "./GlowButton"

const MAX_FILE_SIZE = 10 * 1024 * 1024

const VALID_TYPES = [
	"image/jpeg",
	"image/jpg",
	"image/png",
	"image/webp"
]

function formatFileSize(bytes) {

	if (bytes < 1024) {

		return `${bytes} B`

	}

	if (bytes < 1024 * 1024) {

		return `${(bytes / 1024).toFixed(1)} KB`

	}

	return `${(bytes / (1024 * 1024)).toFixed(2)} MB`

}

function UploadCard({

	selectedFile,

	setSelectedFile

}) {

	const fileInputRef = useRef(null)

	const [dragActive, setDragActive] = useState(false)

	const [error, setError] = useState("")

	const previewUrl = useMemo(() => {

		if (!selectedFile) {

			return null

		}

		return URL.createObjectURL(selectedFile)

	}, [selectedFile])

	useEffect(() => {

		return () => {

			if (previewUrl) {

				URL.revokeObjectURL(previewUrl)

			}

		}

	}, [previewUrl])

	const validateFile = (file) => {

		if (!VALID_TYPES.includes(file.type)) {

			setError(
				"Only JPG, JPEG, PNG and WEBP images are supported."
			)

			return false

		}

		if (file.size > MAX_FILE_SIZE) {

			setError(
				"Maximum file size is 10 MB."
			)

			return false

		}

		setError("")

		return true

	}

	const handleFile = (file) => {

		if (!file) {

			return

		}

		if (!validateFile(file)) {

			return

		}

		setSelectedFile(file)

	}

	const handleBrowse = () => {

		fileInputRef.current?.click()

	}

	const handleFileChange = (event) => {

		handleFile(
			event.target.files[0]
		)

	}

	const handleDragOver = (event) => {

		event.preventDefault()

		setDragActive(true)

	}

	const handleDragLeave = (event) => {

		event.preventDefault()

		setDragActive(false)

	}

	const handleDrop = (event) => {

		event.preventDefault()

		setDragActive(false)

		handleFile(
			event.dataTransfer.files[0]
		)

	}

	const handleRemove = () => {

		setSelectedFile(null)

		setError("")

		if (fileInputRef.current) {

			fileInputRef.current.value = ""

		}

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

			<AnimatePresence mode="wait">

				{

					selectedFile ? (

						<motion.div

							key="preview"

							initial={{
								opacity: 0,
								scale: 0.96
							}}

							animate={{
								opacity: 1,
								scale: 1
							}}

							exit={{
								opacity: 0,
								scale: 0.96
							}}

							className="
	flex
	flex-col
	items-center

	rounded-3xl

	border
	border-green-300

	bg-gradient-to-br
	from-green-50
	to-white

	p-8

	transition-all
	duration-300

	dark:border-green-500/20

	dark:bg-none
	dark:from-transparent
	dark:to-transparent

	dark:bg-[rgba(17,27,22,0.75)]
	dark:backdrop-blur-xl
"

						>

							<div
	className="
		group
		w-full
		overflow-hidden
		rounded-xl
border
border-green-200

dark:border-green-500/20
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
			transition-transform
			duration-500
			group-hover:scale-105
		"

	/>

</div>

<div
	className="
		mt-5
		w-full
		space-y-4
	"
>

	<div
		className="
			flex
			items-start
			justify-between
			gap-4
		"
	>

		<div className="min-w-0">

			<h3
				className="
					truncate
					text-lg
					font-semibold
					text-gray-800
					dark:text-white
				"
			>

				{selectedFile.name}

			</h3>

			<p
				className="
					mt-1
					text-sm
					text-gray-500
					dark:text-gray-400
				"
			>

				{formatFileSize(selectedFile.size)}

			</p>

		</div>

		<div
			className="
				flex
				items-center
				gap-2
				rounded-full
				bg-green-100
				px-4
				py-2
				text-sm
				font-semibold
				text-green-700

				dark:bg-green-500/15
				dark:text-green-300
			"
		>

			<FaCheckCircle />

			<span>

				Ready

			</span>

		</div>

	</div>

</div>

							<div
								className="
									mt-6
									grid
									w-full
									gap-4
									sm:grid-cols-2
								"
							>
                            								<GlowButton
									onClick={handleBrowse}
								>

									Change Image

								</GlowButton>

								<GlowButton

									onClick={handleRemove}

									className="
										bg-gradient-to-r
										from-red-500
										to-red-400
										shadow-red-500/30
										hover:shadow-red-400/60
									"

								>

									<div
										className="
											flex
											items-center
											justify-center
											gap-2
										"
									>

										<FaTrash />

										<span>

											Remove Image

										</span>

									</div>

								</GlowButton>

							</div>

						</motion.div>

					) : (

						<motion.div

							key="upload"

							initial={{
								opacity: 0,
								scale: 0.96
							}}

							animate={{
								opacity: 1,
								scale: 1
							}}

							exit={{
								opacity: 0
							}}

							onDragOver={handleDragOver}

							onDragLeave={handleDragLeave}

							onDrop={handleDrop}

							className={`
								flex
								flex-col
								items-center
								justify-center
								rounded-3xl
								border-2
								border-dashed
								p-12
								text-center
								transition-all
								duration-300

								${
									dragActive

										? `
											border-green-500
											bg-green-100
											shadow-[0_0_40px_rgba(34,197,94,0.30)]

											dark:bg-green-500/10
											dark:shadow-[0_0_50px_rgba(34,197,94,0.35)]
										`

										: `
											border-green-300
											bg-green-50
											hover:border-green-500
											hover:bg-green-100
											hover:shadow-[0_0_30px_rgba(34,197,94,0.25)]

											dark:border-green-500/25
											dark:bg-white/5
											dark:hover:bg-green-500/10
											dark:hover:border-green-400
											dark:hover:shadow-[0_0_45px_rgba(34,197,94,0.30)]
										`
								}
							`}

						>

							<motion.div

								animate={{
									y: [0, -8, 0]
								}}

								transition={{
									duration: 2,
									repeat: Infinity
								}}

							>

								<FaCloudUploadAlt
									className="
										text-7xl
										text-green-600
										dark:text-green-400
									"
								/>

							</motion.div>

							<h2
								className="
									mt-6
									text-3xl
									font-bold
									text-gray-800
									transition-colors

									dark:text-white
								"
							>

								Upload Plant Image

							</h2>

							<p
								className="
									mt-4
									max-w-md
									text-gray-500
									transition-colors

									dark:text-gray-400
								"
							>

								Drag & Drop your plant image here or browse from your computer.

							</p>

							<div
								className="
									mt-6
									w-60
								"
							>

								<GlowButton
									onClick={handleBrowse}
								>

									Browse Files

								</GlowButton>

							</div>

							<div
								className="
									mt-8
									flex
									flex-wrap
									items-center
									justify-center
									gap-3
									text-sm
									text-gray-500

									dark:text-gray-400
								"
							>

								<div>

									JPG

								</div>

								<div>•</div>

								<div>PNG</div>

								<div>•</div>

								<div>WEBP</div>

								<div>•</div>

								<div>Max 10 MB</div>

							</div>

							{

								error && (

									<div
										className="
											mt-6
											flex
											items-center
											gap-3
											rounded-xl
											border
											border-red-300
											bg-red-50
											p-4
											text-red-700

											dark:border-red-500/30
											dark:bg-red-500/10
											dark:text-red-300
										"
									>

										<FaExclamationTriangle />

										<span>

											{error}

										</span>

									</div>

								)

							}

						</motion.div>

					)

				}

			</AnimatePresence>

		</GlassCard>

	)

}

export default UploadCard