from typing import Dict
from .base import APIBase


class TokenAPI(APIBase):
    """Token-related methods"""

    def get_token_account_balance(self, pubkey: str, commitment: str = None) -> Dict:
        """
        Returns the token balance of an SPL Token account.

        Args:
            pubkey (str): Public key of the token account to query
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Token account balance information
        """
        params = [pubkey]

        if commitment:
            params.append({"commitment": commitment})

        return self._make_request("getTokenAccountBalance", params)

    def get_token_accounts_by_delegate(
        self,
        delegate: str,
        mint: str = None,
        program_id: str = None,
        encoding: str = "jsonParsed",
        commitment: str = None,
    ) -> Dict:
        """
        Returns all SPL Token accounts by approved Delegate.

        Args:
            delegate (str): Delegate address to query
            mint (str, optional): The mint to filter accounts by
            program_id (str, optional): The program ID to filter accounts by
            encoding (str, optional): Encoding format for the response
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Token accounts by delegate information
        """
        params = [delegate]

        if mint:
            params.append({"mint": mint})
        elif program_id:
            params.append({"programId": program_id})
        else:
            return {"error": "Either mint or programId must be provided"}

        config = {"encoding": encoding}
        if commitment:
            config["commitment"] = commitment

        params.append(config)

        return self._make_request("getTokenAccountsByDelegate", params)

    def get_token_accounts_by_owner(
        self,
        owner: str,
        mint: str = None,
        program_id: str = None,
        encoding: str = "jsonParsed",
        commitment: str = None,
    ) -> Dict:
        """
        Returns all SPL Token accounts by token owner.

        Args:
            owner (str): Owner address to query
            mint (str, optional): The mint to filter accounts by
            program_id (str, optional): The program ID to filter accounts by
            encoding (str, optional): Encoding format for the response
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Token accounts by owner information
        """
        params = [owner]

        if mint:
            params.append({"mint": mint})
        elif program_id:
            params.append({"programId": program_id})
        else:
            return {"error": "Either mint or programId must be provided"}

        config = {"encoding": encoding}
        if commitment:
            config["commitment"] = commitment

        params.append(config)

        return self._make_request("getTokenAccountsByOwner", params)

    def get_token_largest_accounts(self, mint: str, commitment: str = None) -> Dict:
        """
        Returns the 20 largest accounts of a particular SPL Token type.

        Args:
            mint (str): Token mint address to query
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Largest token accounts information
        """
        params = [mint]

        if commitment:
            params.append({"commitment": commitment})

        return self._make_request("getTokenLargestAccounts", params)

    def get_token_supply(self, mint: str, commitment: str = None) -> Dict:
        """
        Returns the total supply of an SPL Token type.

        Args:
            mint (str): Token mint address to query
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Token supply information
        """
        params = [mint]

        if commitment:
            params.append({"commitment": commitment})

        return self._make_request("getTokenSupply", params)
