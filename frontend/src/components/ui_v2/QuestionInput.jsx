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
						text-gray-800
						outline-none
						transition-colors
						duration-300

						placeholder:text-gray-400

						dark:text-gray-100
						dark:placeholder:text-gray-500
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

						shadow-lg
						shadow-green-500/25

						transition-all
						duration-300

						hover:scale-110
						hover:bg-green-700
						hover:shadow-green-500/40

						active:scale-95

						dark:bg-green-500
						dark:hover:bg-green-400
					"

				>

					<FaArrowRight />

				</button>

			</div>

		</GlassCard>

	)

}

export default QuestionInput