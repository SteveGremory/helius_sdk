from sdk.rpc import HeliusRPC

# Initialize the client with your API key
helius = HeliusRPC("API_KEY")

# Using the Account API
balance = helius.account.get_balance("KEY")
account_info = helius.account.get_account_info("KEY")
multi_accounts = helius.account.get_multiple_accounts(
    [
        "KEY1",
        "KEY2",
    ]
)
program_accounts = helius.account.get_program_accounts("KEY")

# Using the Block API
block = helius.block.get_block(430)
block_time = helius.block.get_block_time(430)
blocks = helius.block.get_blocks(100, 150)
block_height = helius.block.get_block_height(commitment="finalized")

# Using the Cluster API
nodes = helius.cluster.get_cluster_nodes()
epoch_info = helius.cluster.get_epoch_info()
slot = helius.cluster.get_slot()
identity = helius.cluster.get_identity()
health = helius.cluster.get_health()

# Using the Token API
token_balance = helius.token.get_token_account_balance("KEY")
token_accounts = helius.token.get_token_accounts_by_owner(
    "KEY",
    program_id="PROGRAM_ID",
)
token_supply = helius.token.get_token_supply("MINT")

# Using the Transaction API
latest_blockhash = helius.transaction.get_latest_blockhash()
signatures = helius.transaction.get_signatures_for_address(
    "Vote111111111111111111111111111111111111111", limit=5
)
transaction_details = helius.transaction.get_transaction("SIGNATURE")
tx_count = helius.transaction.get_transaction_count()

# Using the Staking API
inflation_rate = helius.staking.get_inflation_rate()
supply = helius.staking.get_supply()
vote_accounts = helius.staking.get_vote_accounts()

# Using the Performance API
performance_samples = helius.performance.get_recent_performance_samples(10)
