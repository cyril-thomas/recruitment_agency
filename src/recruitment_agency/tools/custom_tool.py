from crewai.tools import BaseTool, tool
from typing import Type, Optional
from pydantic import BaseModel, Field
import requests
import json


class PostToAPIToolInput(BaseModel):
    """Input needed for post to the API."""

    data: dict = Field(
        ..., description="The data dictionary to be sent in the request body."
    )


class PostToAPITool(BaseTool):
    name: str = "Post to an API Tool"
    description: str = (
        """
        Send a POST request to a REST API endpoint with JSON data.
        
        Args:
            endpoint_url (str): The URL of the API endpoint
            data (dict): The data to be sent in the request body
            headers (dict, optional): Additional headers to include in the request
            
        Returns:
            status: The response status from the API
    """
    )
    args_schema: Type[BaseModel] = PostToAPIToolInput
    endpoint_url: str = Field(..., description="Mandatory URL of the API endpoint")
    headers: Optional[dict] = Field(
        ..., description="Additional headers to include in the request"
    )

    def _run(self, data: dict) -> int:
        # Default headers if none provided
        if self.headers is None:
            headers = {"Content-Type": "application/json", "Accept": "application/json"}
        else:
            headers = self.headers

        try:
            # Convert the data dictionary to a JSON string
            json_data = json.dumps(data)

            # Send POST request
            response = requests.post(
                url=self.endpoint_url,
                data=json_data,
                headers=headers,
                timeout=30,  # Adding timeout for better error handling
            )

            # Raise an exception for bad status codes
            response.raise_for_status()

            # Return the response object
            return response.status_code

        except requests.exceptions.RequestException as e:
            print(f"Error making API request: {str(e)}")
            raise
        except json.JSONDecodeError as e:
            print(f"Error encoding JSON data: {str(e)}")
            raise
