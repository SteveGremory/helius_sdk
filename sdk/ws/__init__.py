from sdk.ws.wrappers.account import AccountSubscriptionWS
from sdk.ws.wrappers.program import ProgramSubscriptionWS
from sdk.ws.wrappers.logs import LogsSubscriptionWS
from sdk.ws.wrappers.signature import SignatureSubscriptionWS
from sdk.ws.wrappers.blockchain_state import BlockchainStateWS
from sdk.ws.wrappers.unstable import UnstableSubscriptionWS


class WS(
    AccountSubscriptionWS,
    ProgramSubscriptionWS,
    LogsSubscriptionWS,
    SignatureSubscriptionWS,
    BlockchainStateWS,
    UnstableSubscriptionWS,
):
    """
    A Python wrapper for  WebSocket API.

    This class provides methods for subscribing to different types of real-time updates
    from the Solana blockchain through  WebSocket API.
    """

    pass
