from .base import APIBase
from typing import List, Dict, Union, Optional, Any


class AccountAPI(APIBase):
    """Account-related methods"""

    def get_account_info(
        self, pubkey: str, encoding: str = "base58", commitment: str = None
    ) -> Dict:
        """
        Returns all information associated with the account of provided Pubkey.

        Args:
            pubkey (str): Public key of the account to query
            encoding (str, optional): Encoding for the returned data (base58, base64, jsonParsed)
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Account information
        """
        params = [pubkey, {"encoding": encoding}]

        if commitment:
            params[1]["commitment"] = commitment

        return self._make_request("getAccountInfo", params)

    def get_balance(self, pubkey: str, commitment: str = None) -> Dict:
        """
        Returns the lamport balance of the account of provided Pubkey.

        Args:
            pubkey (str): Public key of the account to query
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Account balance information
        """
        params = [pubkey]

        if commitment:
            params.append({"commitment": commitment})

        return self._make_request("getBalance", params)

    def get_multiple_accounts(
        self, pubkeys: List[str], encoding: str = "base58", commitment: str = None
    ) -> Dict:
        """
        Returns the account information for a list of Pubkeys.

        Args:
            pubkeys (List[str]): List of public keys to query
            encoding (str, optional): Encoding for the returned data
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Multiple account information
        """
        params = [pubkeys]

        config = {"encoding": encoding}
        if commitment:
            config["commitment"] = commitment

        params.append(config)

        return self._make_request("getMultipleAccounts", params)

    def get_program_accounts(
        self,
        programId: str,
        encoding: str = "base58",
        filters: List = None,
        commitment: str = None,
    ) -> Dict:
        """
        Returns all accounts owned by the provided program Pubkey.

        Args:
            programId (str): Public key of the program to query
            encoding (str, optional): Encoding for the returned data
            filters (List, optional): List of filter objects
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Program accounts information
        """
        config = {"encoding": encoding}
        if commitment:
            config["commitment"] = commitment

        params = [programId]

        if filters:
            config["filters"] = filters

        params.append(config)

        return self._make_request("getProgramAccounts", params)

    def get_minimum_balance_for_rent_exemption(
        self, data_size: int, commitment: str = None
    ) -> Dict:
        """
        Returns minimum balance required to make account rent exempt.

        Args:
            data_size (int): Size of data in the account
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Minimum balance for rent exemption
        """
        params = [data_size]

        if commitment:
            params.append({"commitment": commitment})

        return self._make_request("getMinimumBalanceForRentExemption", params)

    def request_airdrop(
        self, pubkey: str, lamports: int, commitment: str = None
    ) -> Dict:
        """
        Requests an airdrop of lamports to a Pubkey.

        Args:
            pubkey (str): Public key to receive lamports
            lamports (int): Amount of lamports to airdrop
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Airdrop transaction signature
        """
        params = [pubkey, lamports]

        if commitment:
            params.append({"commitment": commitment})

        return self._make_request("requestAirdrop", params)
