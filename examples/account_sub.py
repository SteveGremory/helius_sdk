from sdk.ws import HeliusWS
import asyncio


async def main():
    client = HeliusWS("wss://mainnet.helius-rpc.com", "API_KEY")
    await client.connect()

    sub_id = await client.account_subscribe(
        "PUB_KEY",
        {"encoding": "jsonParsed", "commitment": "finalized"},
    )

    async def handle_notification(data):
        print(f"Received: {data}")
        print("")

    await client.handle_notifications(handle_notification)


if __name__ == "__main__":

    asyncio.run(main())
