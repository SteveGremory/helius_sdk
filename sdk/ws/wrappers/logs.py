from .base import BaseWS


class LogsSubscriptionWS(BaseWS):
    """
    Handles logs-related subscriptions.
    """

    async def logs_subscribe(self, filter_type, config=None):
        """
        Subscribe to transaction logging.

        Args:
            filter_type (str or dict): The filter criteria.
                - "all": Subscribe to all transactions except for simple vote transactions.
                - "allWithVotes": Subscribe to all transactions, including simple vote transactions.
                - {"mentions": ["pubkey"]}: Subscribe only to transactions mentioning this address.
            config (dict, optional): Configuration options, including commitment level.

        Returns:
            int: The subscription ID.
        """
        params = [filter_type]
        if config:
            params.append(config)

        response = await self._send_request("logsSubscribe", params)
        if "result" in response:
            subscription_id = response["result"]
            self.subscriptions[subscription_id] = "logs"
            return subscription_id
        else:
            raise Exception(f"Error subscribing to logs: {response.get('error')}")

    async def logs_unsubscribe(self, subscription_id):
        """
        Unsubscribe from transaction logging.

        Args:
            subscription_id (int): The subscription ID to cancel.

        Returns:
            bool: True if unsubscribe was successful, False otherwise.
        """
        response = await self._send_request("logsUnsubscribe", [subscription_id])
        if "result" in response:
            if response["result"]:
                self.subscriptions.pop(subscription_id, None)
            return response["result"]
        else:
            raise Exception(f"Error unsubscribing from logs: {response.get('error')}")
