import axios from "axios"

const api = axios.create({
	baseURL: "http://127.0.0.1:8000",
	timeout: 120000,
	headers: {
		"Content-Type": "application/json"
	}
})

export const getWeather = async (
	latitude,
	longitude
) => {

	const response = await api.get(
		"/weather",
		{
			params: {
				latitude,
				longitude
			}
		}
	)

	return response.data

}

export const scanPlant = async (
	formData
) => {

	const response = await api.post(
		"/scan",
		formData,
		{
			headers: {
				"Content-Type": "multipart/form-data"
			}
		}
	)

	return response.data

}

export default api