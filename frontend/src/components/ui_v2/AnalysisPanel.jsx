import { useState } from "react"

import { scanPlant } from "../../services/api"

import UploadCard from "./UploadCard"
import QuestionInput from "./QuestionInput"
import GlowButton from "./GlowButton"
import ResultPanel from "./ResultPanel"

function AnalysisPanel() {

	const [selectedFile, setSelectedFile] = useState(null)

	const [question, setQuestion] = useState("")

	const [loading, setLoading] = useState(false)

	const [result, setResult] = useState(null)

	const [error, setError] = useState("")

	const handleScan = async () => {

		if (!selectedFile) {

			alert("Please select a plant image.")

			return

		}

		try {

			setLoading(true)

			setError("")

			const formData = new FormData()

			formData.append(
				"file",
				selectedFile
			)

			formData.append(
				"query",
				question
			)

			const response = await scanPlant(
				formData
			)

			setResult(
				response
			)

		}

		catch {

			setError(
				"Unable to analyze the plant."
			)

		}

		finally {

			setLoading(false)

		}

	}

	return (

		<div className="mx-auto mt-10 max-w-5xl space-y-6">

			<UploadCard

				selectedFile={selectedFile}

				setSelectedFile={setSelectedFile}

			/>

			<QuestionInput

				question={question}

				setQuestion={setQuestion}

				onSubmit={handleScan}

			/>

			<GlowButton

				onClick={handleScan}

				loading={loading}

			>

				⚡ Analyze Plant

			</GlowButton>

			{

				error && (

					<div
						className="
							rounded-xl
							bg-red-100
							p-4
							text-red-700
						"
					>

						{error}

					</div>

				)

			}

			<ResultPanel

				result={result}

				selectedFile={selectedFile}

			/>

		</div>

	)

}

export default AnalysisPanel