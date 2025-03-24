from .base import BaseHeliusWS


class AccountSubscriptionWS(BaseHeliusWS):
    """
    Handles account-related subscriptions.
    """

    async def account_subscribe(self, pubkey, config=None):
        """
        Subscribe to an account to receive notifications when the lamports or data changes.

        Args:
            pubkey (str): The account public key as a base-58 encoded string.
            config (dict, optional): Configuration options.
                - commitment (str, optional): Commitment level.
                - encoding (str, optional): Data encoding format (base58, base64, base64+zstd, jsonParsed).

        Returns:
            int: The subscription ID.
        """
        params = [pubkey]
        if config:
            params.append(config)

        response = await self._send_request("accountSubscribe", params)
        if "result" in response:
            subscription_id = response["result"]
            self.subscriptions[subscription_id] = "account"
            return subscription_id
        else:
            raise Exception(f"Error subscribing to account: {response.get('error')}")

    async def account_unsubscribe(self, subscription_id):
        """
        Unsubscribe from account change notifications.

        Args:
            subscription_id (int): The subscription ID to cancel.

        Returns:
            bool: True if unsubscribe was successful, False otherwise.
        """
        response = await self._send_request("accountUnsubscribe", [subscription_id])
        if "result" in response:
            if response["result"]:
                self.subscriptions.pop(subscription_id, None)
            return response["result"]
        else:
            raise Exception(
                f"Error unsubscribing from account: {response.get('error')}"
            )
