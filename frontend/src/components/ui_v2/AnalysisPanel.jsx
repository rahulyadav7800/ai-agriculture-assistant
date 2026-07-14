import { useRef, useState } from "react"

import { scanPlant } from "../../services/api"

import UploadCard from "./UploadCard"
import QuestionInput from "./QuestionInput"
import GlowButton from "./GlowButton"
import ResultPanel from "./ResultPanel"
import LoadingScreen from "./LoadingScreen"

function AnalysisPanel() {

	const [selectedFile, setSelectedFile] = useState(null)

	const [question, setQuestion] = useState("")

	const [loading, setLoading] = useState(false)

	const [result, setResult] = useState(null)

	const [error, setError] = useState("")

	const resultRef = useRef(null)

	const handleScan = async () => {

		if (!selectedFile) {

			alert("Please select a plant image.")

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

			const response = await scanPlant(
				formData
			)

			setResult(response)

			setTimeout(() => {

				resultRef.current?.scrollIntoView({

					behavior: "smooth",

					block: "start"

				})

			}, 200)

		}

		catch (error) {

			console.error(error)

			setError(

				error.response?.data?.detail ||

				"Unable to analyze the plant."

			)

		}

		finally {

			setLoading(false)

		}

	}

	return (

		<div
			className="
				mx-auto
				mt-10
				max-w-5xl
				space-y-6
			"
		>

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
							border
							border-red-200
							bg-red-50
							p-4
							text-red-700
						"
					>

						{error}

					</div>

				)

			}

			<div ref={resultRef}>

				{

					loading ? (

						<LoadingScreen />

					) : (

						<ResultPanel

							result={result}

							selectedFile={selectedFile}

						/>

					)

				}

			</div>

		</div>

	)

}

export default AnalysisPanel