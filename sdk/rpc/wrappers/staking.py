from typing import List, Dict
from .base import APIBase


class StakingAPI(APIBase):
    """Staking-related methods"""

    def get_inflation_governor(self, commitment: str = None) -> Dict:
        """
        Returns the current inflation governor.

        Args:
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Inflation governor information
        """
        params = []

        if commitment:
            params.append({"commitment": commitment})

        return self._make_request("getInflationGovernor", params if params else None)

    def get_inflation_rate(self) -> Dict:
        """
        Returns the specific inflation values for the current epoch.

        Returns:
            Dict: Inflation rate information
        """
        return self._make_request("getInflationRate")

    def get_inflation_reward(
        self,
        addresses: List[str],
        epoch: int = None,
        commitment: str = None,
        min_context_slot: int = None,
    ) -> Dict:
        """
        Returns the inflation / staking reward for a list of addresses for an epoch.

        Args:
            addresses (List[str]): List of addresses to query
            epoch (int, optional): Epoch for which to calculate rewards
            commitment (str, optional): Commitment level to use
            min_context_slot (int, optional): The minimum slot that the request can be evaluated at

        Returns:
            Dict: Inflation reward information
        """
        params = [addresses]

        if any([epoch is not None, commitment, min_context_slot is not None]):
            config = {}
            if epoch is not None:
                config["epoch"] = epoch
            if commitment:
                config["commitment"] = commitment
            if min_context_slot is not None:
                config["minContextSlot"] = min_context_slot

            params.append(config)

        return self._make_request("getInflationReward", params)

    def get_largest_accounts(
        self, filter_type: str = None, commitment: str = None
    ) -> Dict:
        """
        Returns the 20 largest accounts, by lamport balance.

        Args:
            filter_type (str, optional): Filter results by account type (circulating|nonCirculating)
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Largest accounts information
        """
        params = []

        if filter_type or commitment:
            config = {}
            if filter_type:
                config["filter"] = filter_type
            if commitment:
                config["commitment"] = commitment

            params.append(config)

        return self._make_request("getLargestAccounts", params if params else None)

    def get_stake_minimum_delegation(self, commitment: str = None) -> Dict:
        """
        Returns the stake minimum delegation, in lamports.

        Args:
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Stake minimum delegation information
        """
        params = []

        if commitment:
            params.append({"commitment": commitment})

        return self._make_request(
            "getStakeMinimumDelegation", params if params else None
        )

    def get_supply(
        self,
        commitment: str = None,
        exclude_non_circulating_accounts_list: bool = False,
    ) -> Dict:
        """
        Returns information about the current supply.

        Args:
            commitment (str, optional): Commitment level to use
            exclude_non_circulating_accounts_list (bool, optional): Exclude non-circulating accounts list from response

        Returns:
            Dict: Supply information
        """
        params = []

        if commitment or exclude_non_circulating_accounts_list:
            config = {}
            if commitment:
                config["commitment"] = commitment
            if exclude_non_circulating_accounts_list:
                config["excludeNonCirculatingAccountsList"] = True

            params.append(config)

        return self._make_request("getSupply", params if params else None)

    def get_vote_accounts(
        self,
        commitment: str = None,
        keep_unstaked_delinquents: bool = None,
        delinquent_slot_distance: int = None,
        vote_pubkey: str = None,
    ) -> Dict:
        """
        Returns the account info and associated stake for all the voting accounts in the current bank.

        Args:
            commitment (str, optional): Commitment level to use
            keep_unstaked_delinquents (bool, optional): Keep delinquent validators with no stake
            delinquent_slot_distance (int, optional): Override for delinquent slot distance
            vote_pubkey (str, optional): Only return results for this vote account pubkey

        Returns:
            Dict: Vote accounts information
        """
        params = []

        if any(
            [
                commitment,
                keep_unstaked_delinquents is not None,
                delinquent_slot_distance is not None,
                vote_pubkey,
            ]
        ):
            config = {}
            if commitment:
                config["commitment"] = commitment
            if keep_unstaked_delinquents is not None:
                config["keepUnstakedDelinquents"] = keep_unstaked_delinquents
            if delinquent_slot_distance is not None:
                config["delinquentSlotDistance"] = delinquent_slot_distance
            if vote_pubkey:
                config["votePubkey"] = vote_pubkey

            params.append(config)

        return self._make_request("getVoteAccounts", params if params else None)
