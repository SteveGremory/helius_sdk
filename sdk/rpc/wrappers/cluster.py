from typing import Dict
from .base import APIBase


class ClusterAPI(APIBase):
    """Cluster-related methods"""

    def get_cluster_nodes(self) -> Dict:
        """
        Returns information about all the nodes participating in the cluster.

        Returns:
            Dict: Cluster node information
        """
        return self._make_request("getClusterNodes")

    def get_epoch_info(
        self, commitment: str = None, min_context_slot: int = None
    ) -> Dict:
        """
        Returns information about the current epoch.

        Args:
            commitment (str, optional): Commitment level to use
            min_context_slot (int, optional): The minimum slot that the request can be evaluated at

        Returns:
            Dict: Epoch information
        """
        params = []

        if commitment or min_context_slot is not None:
            config = {}
            if commitment:
                config["commitment"] = commitment
            if min_context_slot is not None:
                config["minContextSlot"] = min_context_slot

            params.append(config)

        return self._make_request("getEpochInfo", params if params else None)

    def get_epoch_schedule(self) -> Dict:
        """
        Returns the epoch schedule information from this cluster's genesis config.

        Returns:
            Dict: Epoch schedule information
        """
        return self._make_request("getEpochSchedule")

    def get_genesis_hash(self) -> Dict:
        """
        Returns the genesis hash.

        Returns:
            Dict: Genesis hash
        """
        return self._make_request("getGenesisHash")

    def get_health(self) -> Dict:
        """
        Returns the current health of the node.

        Returns:
            Dict: Node health information
        """
        return self._make_request("getHealth")

    def get_identity(self) -> Dict:
        """
        Returns the identity pubkey for the current node.

        Returns:
            Dict: Node identity information
        """
        return self._make_request("getIdentity")

    def get_version(self) -> Dict:
        """
        Returns the current Solana version running on the node.

        Returns:
            Dict: Solana version details
        """
        return self._make_request("getVersion")

    def get_slot(self, commitment: str = None, min_context_slot: int = None) -> Dict:
        """
        Returns the slot that has reached the given or default commitment level.

        Args:
            commitment (str, optional): Commitment level to use
            min_context_slot (int, optional): The minimum slot that the request can be evaluated at

        Returns:
            Dict: Current slot
        """
        params = []

        if commitment or min_context_slot is not None:
            config = {}
            if commitment:
                config["commitment"] = commitment
            if min_context_slot is not None:
                config["minContextSlot"] = min_context_slot

            params.append(config)

        return self._make_request("getSlot", params if params else None)

    def get_slot_leader(
        self, commitment: str = None, min_context_slot: int = None
    ) -> Dict:
        """
        Returns the current slot leader.

        Args:
            commitment (str, optional): Commitment level to use
            min_context_slot (int, optional): The minimum slot that the request can be evaluated at

        Returns:
            Dict: Slot leader information
        """
        params = []

        if commitment or min_context_slot is not None:
            config = {}
            if commitment:
                config["commitment"] = commitment
            if min_context_slot is not None:
                config["minContextSlot"] = min_context_slot

            params.append(config)

        return self._make_request("getSlotLeader", params if params else None)

    def get_slot_leaders(self, start_slot: int, limit: int) -> Dict:
        """
        Returns the slot leaders for a given slot range.

        Args:
            start_slot (int): Start slot
            limit (int): Limit (between 1 and 5000)

        Returns:
            Dict: Slot leaders information
        """
        return self._make_request("getSlotLeaders", [start_slot, limit])

    def get_max_retransmit_slot(self) -> Dict:
        """
        Get the max slot seen from retransmit stage.

        Returns:
            Dict: Max retransmit slot
        """
        return self._make_request("getMaxRetransmitSlot")

    def get_max_shred_insert_slot(self) -> Dict:
        """
        Get the max slot seen from after shred insert.

        Returns:
            Dict: Max shred insert slot
        """
        return self._make_request("getMaxShredInsertSlot")
