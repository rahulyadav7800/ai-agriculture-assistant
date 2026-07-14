import { FaArrowRight } from "react-icons/fa"

import GlassCard from "./GlassCard"

function QuestionInput({

	question,

	setQuestion,

	onSubmit

}) {

	const handleKeyDown = (event) => {

		if (event.key === "Enter") {

			event.preventDefault()

			onSubmit?.()

		}

	}

	return (

		<GlassCard>

			<div className="flex items-center gap-4">

				<input

					type="text"

					value={question}

					onChange={(event) =>

						setQuestion(
							event.target.value
						)

					}

					onKeyDown={handleKeyDown}

					placeholder="Ask anything about your plant..."

					className="
						flex-1
						border-none
						bg-transparent
						text-lg
						outline-none
						placeholder:text-gray-400
					"

				/>

				<button

					onClick={onSubmit}

					className="
						flex
						h-12
						w-12
						items-center
						justify-center
						rounded-full
						bg-green-600
						text-white
						transition
						duration-300
						hover:scale-110
						hover:bg-green-700
					"

				>

					<FaArrowRight />

				</button>

			</div>

		</GlassCard>

	)

}

export default QuestionInput