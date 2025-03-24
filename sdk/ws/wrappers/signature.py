from .base import BaseHeliusWS


class SignatureSubscriptionWS(BaseHeliusWS):
    """
    Handles signature-related subscriptions.
    """

    async def signature_subscribe(self, signature, config=None):
        """
        Subscribe to receive a notification when the transaction with the given signature
        reaches the specified commitment level.

        Args:
            signature (str): The transaction signature as a base-58 encoded string.
            config (dict, optional): Configuration options.
                - commitment (str, optional): Commitment level.
                - enableReceivedNotification (bool, optional): Whether to subscribe for received notifications.

        Returns:
            int: The subscription ID.
        """
        params = [signature]
        if config:
            params.append(config)

        response = await self._send_request("signatureSubscribe", params)
        if "result" in response:
            subscription_id = response["result"]
            self.subscriptions[subscription_id] = "signature"
            return subscription_id
        else:
            raise Exception(f"Error subscribing to signature: {response.get('error')}")

    async def signature_unsubscribe(self, subscription_id):
        """
        Unsubscribe from signature confirmation notification.

        Args:
            subscription_id (int): The subscription ID to cancel.

        Returns:
            bool: True if unsubscribe was successful, False otherwise.
        """
        response = await self._send_request("signatureUnsubscribe", [subscription_id])
        if "result" in response:
            if response["result"]:
                self.subscriptions.pop(subscription_id, None)
            return response["result"]
        else:
            raise Exception(
                f"Error unsubscribing from signature: {response.get('error')}"
            )
