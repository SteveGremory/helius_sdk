from .base import BaseWS


class BlockchainStateWS(BaseWS):
    """
    Handles blockchain state subscriptions like slots, roots, and blocks.
    """

    async def slot_subscribe(self):
        """
        Subscribe to receive notification anytime a slot is processed by the validator.

        Returns:
            int: The subscription ID.
        """
        response = await self._send_request("slotSubscribe")
        if "result" in response:
            subscription_id = response["result"]
            self.subscriptions[subscription_id] = "slot"
            return subscription_id
        else:
            raise Exception(f"Error subscribing to slot: {response.get('error')}")

    async def slot_unsubscribe(self, subscription_id):
        """
        Unsubscribe from slot notifications.

        Args:
            subscription_id (int): The subscription ID to cancel.

        Returns:
            bool: True if unsubscribe was successful, False otherwise.
        """
        response = await self._send_request("slotUnsubscribe", [subscription_id])
        if "result" in response:
            if response["result"]:
                self.subscriptions.pop(subscription_id, None)
            return response["result"]
        else:
            raise Exception(f"Error unsubscribing from slot: {response.get('error')}")

    async def root_subscribe(self):
        """
        Subscribe to receive notification anytime a new root is set by the validator.

        Returns:
            int: The subscription ID.
        """
        response = await self._send_request("rootSubscribe")
        if "result" in response:
            subscription_id = response["result"]
            self.subscriptions[subscription_id] = "root"
            return subscription_id
        else:
            raise Exception(f"Error subscribing to root: {response.get('error')}")

    async def root_unsubscribe(self, subscription_id):
        """
        Unsubscribe from root notifications.

        Args:
            subscription_id (int): The subscription ID to cancel.

        Returns:
            bool: True if unsubscribe was successful, False otherwise.
        """
        response = await self._send_request("rootUnsubscribe", [subscription_id])
        if "result" in response:
            if response["result"]:
                self.subscriptions.pop(subscription_id, None)
            return response["result"]
        else:
            raise Exception(f"Error unsubscribing from root: {response.get('error')}")

    async def block_subscribe(self, filter_type, config=None):
        """
        Subscribe to receive notification anytime a new block is confirmed or finalized.
        NOTE: This method is marked as unstable in Solana documentation and is not supported by .

        Args:
            filter_type (str or dict): The filter criteria ("all" or {"mentionsAccountOrProgram": "pubkey"}).
            config (dict, optional): Configuration options.

        Returns:
            int: The subscription ID.
        """
        print("WARNING: blockSubscribe is marked as unstable and is not supported by .")
        params = [filter_type]
        if config:
            params.append(config)

        response = await self._send_request("blockSubscribe", params)
        if "result" in response:
            subscription_id = response["result"]
            self.subscriptions[subscription_id] = "block"
            return subscription_id
        else:
            raise Exception(f"Error subscribing to block: {response.get('error')}")

    async def block_unsubscribe(self, subscription_id):
        """
        Unsubscribe from block notifications.

        Args:
            subscription_id (int): The subscription ID to cancel.

        Returns:
            bool: True if unsubscribe was successful, False otherwise.
        """
        response = await self._send_request("blockUnsubscribe", [subscription_id])
        if "result" in response:
            if response["result"]:
                self.subscriptions.pop(subscription_id, None)
            return response["result"]
        else:
            raise Exception(f"Error unsubscribing from block: {response.get('error')}")
