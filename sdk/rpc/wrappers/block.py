from typing import Dict
from .base import HeliusAPIBase


class BlockAPI(HeliusAPIBase):
    """Block-related methods"""

    def get_block(
        self,
        slot: int,
        encoding: str = None,
        transaction_details: str = None,
        commitment: str = None,
        max_supported_transaction_version: int = None,
    ) -> Dict:
        """
        Returns identity and transaction information about a confirmed block in the ledger.

        Args:
            slot (int): Slot number of the block to query
            encoding (str, optional): Encoding for the returned data
            transaction_details (str, optional): Level of transaction detail to return
            commitment (str, optional): Commitment level to use
            max_supported_transaction_version (int, optional): The max transaction version to return

        Returns:
            Dict: Block information
        """
        params = [slot]

        if any(
            [
                encoding,
                transaction_details,
                commitment,
                max_supported_transaction_version is not None,
            ]
        ):
            config = {}
            if encoding:
                config["encoding"] = encoding
            if transaction_details:
                config["transactionDetails"] = transaction_details
            if commitment:
                config["commitment"] = commitment
            if max_supported_transaction_version is not None:
                config["maxSupportedTransactionVersion"] = (
                    max_supported_transaction_version
                )

            params.append(config)

        return self._make_request("getBlock", params)

    def get_block_commitment(self, block: int) -> Dict:
        """
        Returns commitment for particular block.

        Args:
            block (int): Block number to query

        Returns:
            Dict: Block commitment information
        """
        return self._make_request("getBlockCommitment", [block])

    def get_block_height(
        self, commitment: str = None, min_context_slot: int = None
    ) -> Dict:
        """
        Returns the current block height of the node.

        Args:
            commitment (str, optional): Commitment level to use
            min_context_slot (int, optional): The minimum slot that the request can be evaluated at

        Returns:
            Dict: Current block height
        """
        params = []

        if commitment or min_context_slot is not None:
            config = {}
            if commitment:
                config["commitment"] = commitment
            if min_context_slot is not None:
                config["minContextSlot"] = min_context_slot

            params.append(config)

        return self._make_request("getBlockHeight", params if params else None)

    def get_block_production(
        self,
        identity: str = None,
        first_slot: int = None,
        last_slot: int = None,
        commitment: str = None,
    ) -> Dict:
        """
        Returns recent block production information from the current or previous epoch.

        Args:
            identity (str, optional): Filter production by identity (base-58 encoded)
            first_slot (int, optional): Start slot (inclusive)
            last_slot (int, optional): End slot (inclusive)
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: Block production information
        """
        params = []

        if any([identity, first_slot is not None, last_slot is not None, commitment]):
            config = {}
            if commitment:
                config["commitment"] = commitment
            if identity:
                config["identity"] = identity

            if first_slot is not None or last_slot is not None:
                range_config = {}
                if first_slot is not None:
                    range_config["firstSlot"] = first_slot
                if last_slot is not None:
                    range_config["lastSlot"] = last_slot

                config["range"] = range_config

            params.append(config)

        return self._make_request("getBlockProduction", params if params else None)

    def get_block_time(self, block: int) -> Dict:
        """
        Returns the estimated production time of a block.

        Args:
            block (int): Block number to query

        Returns:
            Dict: Block time information
        """
        return self._make_request("getBlockTime", [block])

    def get_blocks(
        self, start_slot: int, end_slot: int = None, commitment: str = None
    ) -> Dict:
        """
        Returns a list of confirmed blocks between two slots.

        Args:
            start_slot (int): Start slot (inclusive)
            end_slot (int, optional): End slot (inclusive)
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: List of confirmed blocks
        """
        params = [start_slot]

        if end_slot is not None:
            params.append(end_slot)

        if commitment:
            params.append({"commitment": commitment})

        return self._make_request("getBlocks", params)

    def get_blocks_with_limit(
        self, start_slot: int, limit: int, commitment: str = None
    ) -> Dict:
        """
        Returns a list of confirmed blocks starting at the given slot.

        Args:
            start_slot (int): Start slot
            limit (int): Maximum number of blocks to return
            commitment (str, optional): Commitment level to use

        Returns:
            Dict: List of confirmed blocks
        """
        params = [{"start_slot": start_slot, "limit": limit}]

        if commitment:
            params[0]["commitment"] = commitment

        return self._make_request("getBlocksWithLimit", params)

    def get_first_available_block(self) -> Dict:
        """
        Returns the slot of the lowest confirmed block that has not been purged from the ledger.

        Returns:
            Dict: First available block slot
        """
        return self._make_request("getFirstAvailableBlock")

    def minimum_ledger_slot(self) -> Dict:
        """
        Returns the lowest slot that the node has information about in its ledger.

        Returns:
            Dict: Minimum ledger slot
        """
        return self._make_request("minimumLedgerSlot")

    def get_highest_snapshot_slot(self) -> Dict:
        """
        Returns the highest slot information that the node has snapshots for.

        Returns:
            Dict: Highest snapshot slot information
        """
        return self._make_request("getHighestSnapshotSlot")
