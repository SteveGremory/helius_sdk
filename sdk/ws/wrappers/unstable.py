from .base import BaseWS


class UnstableSubscriptionWS(BaseWS):
    """
    Handles unstable subscription types that may not be fully supported by .
    """

    async def slots_updates_subscribe(self):
        """
        Subscribe to receive a notification from the validator on a variety of updates on every slot.
        NOTE: This method is marked as unstable in Solana documentation and is not supported by .

        Returns:
            int: The subscription ID.
        """
        print(
            "WARNING: slotsUpdatesSubscribe is marked as unstable and is not supported by ."
        )
        response = await self._send_request("slotsUpdatesSubscribe")
        if "result" in response:
            subscription_id = response["result"]
            self.subscriptions[subscription_id] = "slots_updates"
            return subscription_id
        else:
            raise Exception(
                f"Error subscribing to slots updates: {response.get('error')}"
            )

    async def slots_updates_unsubscribe(self, subscription_id):
        """
        Unsubscribe from slot-update notifications.

        Args:
            subscription_id (int): The subscription ID to cancel.

        Returns:
            bool: True if unsubscribe was successful, False otherwise.
        """
        response = await self._send_request(
            "slotsUpdatesUnsubscribe", [subscription_id]
        )
        if "result" in response:
            if response["result"]:
                self.subscriptions.pop(subscription_id, None)
            return response["result"]
        else:
            raise Exception(
                f"Error unsubscribing from slots updates: {response.get('error')}"
            )

    async def vote_subscribe(self):
        """
        Subscribe to receive notification anytime a new vote is observed in gossip.
        NOTE: This method is marked as unstable in Solana documentation and is not supported by .

        Returns:
            int: The subscription ID.
        """
        print("WARNING: voteSubscribe is marked as unstable and is not supported by .")
        response = await self._send_request("voteSubscribe")
        if "result" in response:
            subscription_id = response["result"]
            self.subscriptions[subscription_id] = "vote"
            return subscription_id
        else:
            raise Exception(f"Error subscribing to vote: {response.get('error')}")

    async def vote_unsubscribe(self, subscription_id):
        """
        Unsubscribe from vote notifications.

        Args:
            subscription_id (int): The subscription ID to cancel.

        Returns:
            bool: True if unsubscribe was successful, False otherwise.
        """
        response = await self._send_request("voteUnsubscribe", [subscription_id])
        if "result" in response:
            if response["result"]:
                self.subscriptions.pop(subscription_id, None)
            return response["result"]
        else:
            raise Exception(f"Error unsubscribing from vote: {response.get('error')}")
