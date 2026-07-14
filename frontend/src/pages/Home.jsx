import Navbar from "../components/layout/Navbar"

import Hero from "../components/ui_v2/Hero"
import AnalysisPanel from "../components/ui_v2/AnalysisPanel"

function Home() {

	return (

		<div className="min-h-screen bg-green-50">

			<Navbar />

			<main className="mx-auto max-w-7xl p-6">

				<Hero />

				<AnalysisPanel />

			</main>

		</div>

	)

}

export default Home