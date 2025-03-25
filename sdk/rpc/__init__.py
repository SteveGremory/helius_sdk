from sdk.rpc.wrappers.accounts import AccountAPI
from sdk.rpc.wrappers.block import BlockAPI
from sdk.rpc.wrappers.cluster import ClusterAPI
from sdk.rpc.wrappers.token import TokenAPI
from sdk.rpc.wrappers.transaction import TransactionAPI
from sdk.rpc.wrappers.staking import StakingAPI
from sdk.rpc.wrappers.performance import PerformanceAPI
from sdk.rpc.helpers.session import SessionManager

import requests

from typing import Any, Dict


class HeliusRPC:
    """
    A Python wrapper for the Helius RPC API for Solana blockchain.

    This class provides access to all Helius RPC endpoints organized into
    logical subclasses by functionality.
    """

    def __init__(self, api_key: str):
        """
        Initialize the HeliusRPC client with your API key.

        Args:
            api_key (str): Your Helius API key
        """
        self.url = f"https://mainnet.helius-rpc.com/?api-key={api_key}"
        self.headers = {"Content-Type": "application/json"}

        self.account = AccountAPI(self)
        self.block = BlockAPI(self)
        self.cluster = ClusterAPI(self)
        self.token = TokenAPI(self)
        self.transaction = TransactionAPI(self)
        self.staking = StakingAPI(self)
        self.performance = PerformanceAPI(self)

        session_manager = SessionManager()
        self.session = session_manager.create_session("helius", self.url)

    def _make_request(self, method: str, params: Any = None) -> Dict:
        """
        Internal method to make RPC requests to the Helius API.

        Args:
            method (str): The RPC method to invoke
            params (Any, optional): Parameters for the request

        Returns:
            Dict: The JSON response from the API
        """
        payload = {"jsonrpc": "2.0", "id": 1, "method": method}

        if params is not None:
            payload["params"] = params

        response = self.session.post(self.url, headers=self.headers, json=payload)

        return response.json()
