function ScanButton({
	loading,
	onScan
}) {

	return (

		<button
			type="button"
			onClick={onScan}
			disabled={loading}
			className="w-full rounded-lg bg-green-700 py-3 text-lg font-semibold text-white transition hover:bg-green-800 disabled:cursor-not-allowed disabled:bg-gray-400"
		>

			{
				loading
					? "Scanning..."
					: "🔍 Scan Plant"
			}

		</button>

	)

}

export default ScanButton