"""
File: response.py
Version: 2.0
Status: Stable
"""

from typing import Any

from pydantic import BaseModel
from pydantic import Field


class PlantResponse(BaseModel):

	plant_name: str = Field(
		...,
		description="Common name of the plant"
	)

	scientific_name: str = Field(
		...,
		description="Scientific name of the plant"
	)

	family: str = Field(
		...,
		description="Plant family"
	)

	confidence: float = Field(
		...,
		description="Prediction confidence percentage"
	)



class ScanResponse(BaseModel):

	success: bool

	plant: PlantResponse

	diagnosis: dict[str, Any]


class ErrorResponse(BaseModel):

	success: bool = False

	error: str