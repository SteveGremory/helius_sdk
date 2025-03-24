import json
import asyncio
import websockets


class BaseHeliusWS:
    """
    Base class for Helius WebSocket API.

    Provides core functionality for WebSocket connection management
    and request handling.
    """

    def __init__(self, url, api_key=None):
        """
        Initialize the BaseHeliusWS instance.

        Args:
            url (str): The WebSocket URL (wss://mainnet.helius-rpc.com or wss://devnet.helius-rpc.com)
            api_key (str, optional): The Helius API key.
        """
        if api_key:
            self.url = f"{url}/?api-key={api_key}"
        else:
            self.url = url
        self.websocket = None
        self.request_id = 1
        self.subscriptions = {}  # To keep track of subscriptions

    async def connect(self):
        """Connect to the WebSocket."""
        if self.websocket is None or self.websocket.closed:
            self.websocket = await websockets.connect(self.url)

    async def disconnect(self):
        """Disconnect from the WebSocket."""
        if self.websocket and not self.websocket.closed:
            await self.websocket.close()
            self.websocket = None

    async def _send_request(self, method, params=None):
        """
        Send a request to the WebSocket.

        Args:
            method (str): The method name.
            params (list, optional): The parameters for the method.

        Returns:
            dict: The response from the server.
        """
        await self.connect()

        request = {
            "jsonrpc": "2.0",
            "id": self.request_id,
            "method": method,
        }

        if params is not None:
            request["params"] = params

        await self.websocket.send(json.dumps(request))
        self.request_id += 1

        response = await self.websocket.recv()
        return json.loads(response)

    async def start_ping(self, interval=30):
        """
        Start sending ping messages to keep the connection alive.

        Args:
            interval (int): The interval in seconds between pings.
        """
        while self.websocket and not self.websocket.closed:
            try:
                await self.websocket.ping()
                print("Ping sent")
                await asyncio.sleep(interval)
            except Exception as e:
                print(f"Error sending ping: {e}")
                break

    async def handle_notifications(self, callback):
        """
        Handle notifications from the WebSocket.

        Args:
            callback (callable): A function to call with each notification.
        """
        while self.websocket and not self.websocket.closed:
            try:
                message = await self.websocket.recv()
                data = json.loads(message)
                if "method" in data and data["method"].endswith("Notification"):
                    await callback(data)
            except Exception as e:
                print(f"Error handling notification: {e}")
                break
