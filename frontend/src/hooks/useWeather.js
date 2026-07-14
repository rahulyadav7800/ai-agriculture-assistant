import { useEffect, useState } from "react"

import { getWeather } from "../services/api"

function useWeather() {

	const [weather, setWeather] = useState(null)

	const [loading, setLoading] = useState(true)

	const [error, setError] = useState("")

	useEffect(() => {

		if (!navigator.geolocation) {

			setError(
				"Geolocation is not supported."
			)

			setLoading(false)

			return

		}

		navigator.geolocation.getCurrentPosition(

			async (position) => {

				try {

					const data = await getWeather(

						position.coords.latitude,

						position.coords.longitude

					)

					setWeather(
						data
					)

				}

				catch {

					setError(
						"Unable to fetch weather."
					)

				}

				finally {

					setLoading(false)

				}

			},

			() => {

				setError(
					"Location permission denied."
				)

				setLoading(false)

			}

		)

	}, [])

	return {

		weather,

		loading,

		error

	}

}

export default useWeather