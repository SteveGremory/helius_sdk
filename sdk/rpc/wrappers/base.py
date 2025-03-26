from typing import Dict, Any


class APIBase:
    """Base class for  API endpoints"""

    def __init__(self, client):
        """
        Initialize with a reference to the parent client.

        Args:
            client: Parent RPC client instance
        """
        self.client = client

    def _make_request(self, method: str, params: Any = None) -> Dict:
        """
        Internal method to make RPC requests to the  API.

        Args:
            method (str): The RPC method to invoke
            params (Any, optional): Parameters for the request

        Returns:
            Dict: The JSON response from the API
        """
        return self.client._make_request(method, params)
