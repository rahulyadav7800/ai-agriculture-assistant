import { useState } from "react"

import { scanPlant } from "../../services/api"

import ImageUploader from "./ImageUploader"
import QuestionBox from "./QuestionBox"
import ScanButton from "./ScanButton"

import PlantCard from "../result/PlantCard"
import ResponseCard from "../result/ResponseCard"

function ScanSection() {

	const [selectedFile, setSelectedFile] = useState(null)

	const [question, setQuestion] = useState("")

	const [loading, setLoading] = useState(false)

	const [result, setResult] = useState(null)

	const [error, setError] = useState("")

	const handleScan = async () => {

		if (!selectedFile) {

			alert("Please select an image.")

			return

		}

		try {

			setLoading(true)

			setError("")

			setResult(null)

			const formData = new FormData()

			formData.append(
				"file",
				selectedFile
			)

			formData.append(
				"query",
				question
			)

			const data = await scanPlant(
				formData
			)

			setResult(
				data
			)

			console.log(
				data
			)

		}

		catch (error) {

			console.error(
				error
			)

			setError(
				"Scan failed."
			)

		}

		finally {

			setLoading(false)

		}

	}

	return (

		<div className="space-y-8">

			<ImageUploader
				selectedFile={selectedFile}
				setSelectedFile={setSelectedFile}
			/>

			<QuestionBox
				question={question}
				setQuestion={setQuestion}
			/>

			<ScanButton
				loading={loading}
				onScan={handleScan}
			/>

			{
				error && (

					<p className="text-center text-red-600">

						{error}

					</p>

				)
			}

			<PlantCard
				plant={result?.plant}
			/>

			<ResponseCard
				diagnosis={result?.diagnosis}
			/>

		</div>

	)

}

export default ScanSection