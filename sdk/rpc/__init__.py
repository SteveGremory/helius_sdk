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


class RPC:
    """
    A Python wrapper for the  RPC API for Solana blockchain.

    This class provides access to all  RPC endpoints organized into
    logical subclasses by functionality.
    """

    def __init__(self, rpc_url: str):
        """
        Initialize the RPC client with your RPC URL (containing the API key).

        Args:
            rpc_url (str): RPC URL (containing the API key)
        """
        self.url = rpc_url
        self.headers = headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.6",
            "content-type": "application/json",
            "origin": "https://pump.fun",
            "priority": "u=1, i",
            "referer": "https://pump.fun/",
            "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Brave";v="134"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "sec-gpc": "1",
            "solana-client": "js/1.0.0-maintenance",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        }

        self.account = AccountAPI(self)
        self.block = BlockAPI(self)
        self.cluster = ClusterAPI(self)
        self.token = TokenAPI(self)
        self.transaction = TransactionAPI(self)
        self.staking = StakingAPI(self)
        self.performance = PerformanceAPI(self)

        session_manager = SessionManager()
        self.session = session_manager.create_session("", self.url)

    def _make_request(self, method: str, params: Any = None) -> Dict:
        """
        Internal method to make RPC requests to the  API.

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
        print(response.elapsed.total_seconds())

        return response.json()
