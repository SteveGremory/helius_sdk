from typing import List, Dict
from .base import APIBase


class TransactionAPI(APIBase):
    """Transaction-related methods"""

    def get_fee_for_message(self, message: str, commitment: str = None) -> Dict:
        """
        Get the fee the network will charge for a particular Message.

        Args:
            message (str): Base-64 encoded Message
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Fee information
        """
        params = [message]

        if commitment:
            params.append({"commitment": commitment})

        return self._make_request("getFeeForMessage", params)

    def get_latest_blockhash(
        self, commitment: str = None, min_context_slot: int = None
    ) -> Dict:
        """
        Returns the latest blockhash.

        Args:
            commitment (str, optional): Commitment level to use
            min_context_slot (int, optional): The minimum slot that the request can be evaluated at

        Returns:
            Dict: Latest blockhash information
        """
        params = []

        if commitment or min_context_slot is not None:
            config = {}
            if commitment:
                config["commitment"] = commitment
            if min_context_slot is not None:
                config["minContextSlot"] = min_context_slot

            params.append(config)

        return self._make_request("getLatestBlockhash", params if params else None)

    def get_recent_prioritization_fees(self, addresses: List[str] = None) -> Dict:
        """
        Returns a list of prioritization fees from recent blocks.

        Args:
            addresses (List[str], optional): List of addresses to query

        Returns:
            Dict: Recent prioritization fees
        """
        params = []

        if addresses:
            params.append(addresses)

        return self._make_request(
            "getRecentPrioritizationFees", params if params else None
        )

    def get_signature_statuses(
        self, signatures: List[str], search_transaction_history: bool = False
    ) -> Dict:
        """
        Returns the statuses of a list of signatures.

        Args:
            signatures (List[str]): List of transaction signatures to query
            search_transaction_history (bool, optional): If true, search past blocks as well

        Returns:
            Dict: Signature statuses
        """
        params = [signatures]

        if search_transaction_history:
            params.append({"searchTransactionHistory": True})

        return self._make_request("getSignatureStatuses", params)

    def get_signatures_for_address(
        self,
        address: str,
        before: str = None,
        until: str = None,
        limit: int = None,
        commitment: str = None,
        min_context_slot: int = None,
    ) -> Dict:
        """
        Returns signatures for confirmed transactions that include the given address.

        Args:
            address (str): Address to query
            before (str, optional): Start searching from this transaction signature
            until (str, optional): Search until this transaction signature
            limit (int, optional): Maximum number of transaction signatures to return
            commitment (str, optional): Commitment level to use
            min_context_slot (int, optional): The minimum slot that the request can be evaluated at

        Returns:
            Dict: Signatures for the specified address
        """
        params = [address]

        config = {}
        if before:
            config["before"] = before
        if until:
            config["until"] = until
        if limit is not None:
            config["limit"] = limit
        if commitment:
            config["commitment"] = commitment
        if min_context_slot is not None:
            config["minContextSlot"] = min_context_slot

        if config:
            params.append(config)

        return self._make_request("getSignaturesForAddress", params)

    def get_transaction(
        self,
        signature: str,
        encoding: str = None,
        commitment: str = None,
        max_supported_transaction_version: int = None,
    ) -> Dict:
        """
        Returns transaction details for a confirmed transaction.

        Args:
            signature (str): Transaction signature to query
            encoding (str, optional): Encoding for the returned transaction
            commitment (str, optional): Commitment level to use
            max_supported_transaction_version (int, optional): The max transaction version to return

        Returns:
            Dict: Transaction details
        """
        params = [signature]

        if any([encoding, commitment, max_supported_transaction_version is not None]):
            config = {}
            if encoding:
                config["encoding"] = encoding
            if commitment:
                config["commitment"] = commitment
            if max_supported_transaction_version is not None:
                config["maxSupportedTransactionVersion"] = (
                    max_supported_transaction_version
                )

            params.append(config)

        return self._make_request("getTransaction", params)

    def get_transaction_count(
        self, commitment: str = None, min_context_slot: int = None
    ) -> Dict:
        """
        Returns the current Transaction count from the ledger.

        Args:
            commitment (str, optional): Commitment level to use
            min_context_slot (int, optional): The minimum slot that the request can be evaluated at

        Returns:
            Dict: Transaction count
        """
        params = []

        if commitment or min_context_slot is not None:
            config = {}
            if commitment:
                config["commitment"] = commitment
            if min_context_slot is not None:
                config["minContextSlot"] = min_context_slot

            params.append(config)

        return self._make_request("getTransactionCount", params if params else None)

    def is_blockhash_valid(
        self, blockhash: str, commitment: str = None, min_context_slot: int = None
    ) -> Dict:
        """
        Returns whether a blockhash is still valid or not.

        Args:
            blockhash (str): The blockhash to validate
            commitment (str, optional): Commitment level to use
            min_context_slot (int, optional): The minimum slot that the request can be evaluated at

        Returns:
            Dict: Blockhash validity information
        """
        params = [blockhash]

        if commitment or min_context_slot is not None:
            config = {}
            if commitment:
                config["commitment"] = commitment
            if min_context_slot is not None:
                config["minContextSlot"] = min_context_slot

            params.append(config)

        return self._make_request("isBlockhashValid", params)

    def send_transaction(self, transaction: str, opts: Dict = None) -> Dict:
        """
        Submits a signed transaction to the cluster for processing.

        Args:
            transaction (str): Signed transaction as base-64 encoded string
            opts (Dict, optional): Options for sending the transaction

        Returns:
            Dict: Transaction signature
        """
        params = [transaction]

        if opts:
            params.append(opts)

        return self._make_request("sendTransaction", params)

    def simulate_transaction(self, transaction: str, opts: Dict = None) -> Dict:
        """
        Simulate sending a transaction.

        Args:
            transaction (str): Transaction to simulate as base-64 encoded string
            opts (Dict, optional): Options for simulating the transaction

        Returns:
            Dict: Simulation results
        """
        params = [transaction]

        if opts:
            params.append(opts)

        return self._make_request("simulateTransaction", params)
