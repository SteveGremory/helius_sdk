from sdk.rpc import RPC

# Initialize the client with your API key
rpc = RPC("API_KEY")

# Using the Account API
balance = rpc.account.get_balance("KEY")
account_info = rpc.account.get_account_info("KEY")
multi_accounts = rpc.account.get_multiple_accounts(
    [
        "KEY1",
        "KEY2",
    ]
)
program_accounts = rpc.account.get_program_accounts("KEY")

# Using the Block API
block = rpc.block.get_block(430)
block_time = rpc.block.get_block_time(430)
blocks = rpc.block.get_blocks(100, 150)
block_height = rpc.block.get_block_height(commitment="finalized")

# Using the Cluster API
nodes = rpc.cluster.get_cluster_nodes()
epoch_info = rpc.cluster.get_epoch_info()
slot = rpc.cluster.get_slot()
identity = rpc.cluster.get_identity()
health = rpc.cluster.get_health()

# Using the Token API
token_balance = rpc.token.get_token_account_balance("KEY")
token_accounts = rpc.token.get_token_accounts_by_owner(
    "KEY",
    program_id="PROGRAM_ID",
)
token_supply = rpc.token.get_token_supply("MINT")

# Using the Transaction API
latest_blockhash = rpc.transaction.get_latest_blockhash()
signatures = rpc.transaction.get_signatures_for_address(
    "Vote111111111111111111111111111111111111111", limit=5
)
transaction_details = rpc.transaction.get_transaction("SIGNATURE")
tx_count = rpc.transaction.get_transaction_count()

# Using the Staking API
inflation_rate = rpc.staking.get_inflation_rate()
supply = rpc.staking.get_supply()
vote_accounts = rpc.staking.get_vote_accounts()

# Using the Performance API
performance_samples = rpc.performance.get_recent_performance_samples(10)
