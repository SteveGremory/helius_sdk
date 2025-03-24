from .base import BaseHeliusWS


class ProgramSubscriptionWS(BaseHeliusWS):
    """
    Handles program-related subscriptions.
    """

    async def program_subscribe(self, program_id, config=None):
        """
        Subscribe to a program to receive notifications when the lamports or data for an account
        owned by the given program changes.

        Args:
            program_id (str): The program ID as a base-58 encoded string.
            config (dict, optional): Configuration options.
                - commitment (str, optional): Commitment level.
                - encoding (str, optional): Encoding format (base58, base64, base64+zstd, jsonParsed).
                - filters (list, optional): Filters to refine the results.

        Returns:
            int: The subscription ID.
        """
        params = [program_id]
        if config:
            params.append(config)

        response = await self._send_request("programSubscribe", params)
        if "result" in response:
            subscription_id = response["result"]
            self.subscriptions[subscription_id] = "program"
            return subscription_id
        else:
            raise Exception(f"Error subscribing to program: {response.get('error')}")

    async def program_unsubscribe(self, subscription_id):
        """
        Unsubscribe from program-owned account change notifications.

        Args:
            subscription_id (int): The subscription ID to cancel.

        Returns:
            bool: True if unsubscribe was successful, False otherwise.
        """
        response = await self._send_request("programUnsubscribe", [subscription_id])
        if "result" in response:
            if response["result"]:
                self.subscriptions.pop(subscription_id, None)
            return response["result"]
        else:
            raise Exception(
                f"Error unsubscribing from program: {response.get('error')}"
            )
