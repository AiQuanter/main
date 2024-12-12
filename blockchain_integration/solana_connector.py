import logging
from solana.rpc.async_api import AsyncClient
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.rpc.types import TxOpts
from typing import Optional, Any

logger = logging.getLogger(__name__)

class SolanaConnector:
    def __init__(self, rpc_url: str = "https://api.mainnet-beta.solana.com"):
        """
        Initializes Solana connection with the specified RPC URL.
        """
        self.client = AsyncClient(rpc_url)
        logger.info(f"Connected to Solana RPC at {rpc_url}")

    async def get_balance(self, wallet_address: str) -> Optional[int]:
        """
        Fetches the balance of the specified wallet address in lamports.
        """
        try:
            public_key = PublicKey(wallet_address)
            response = await self.client.get_balance(public_key)
            balance = response['result']['value']
            logger.info(f"Balance for {wallet_address}: {balance} lamports")
            return balance
        except Exception as e:
            logger.error(f"Error fetching balance for {wallet_address}: {e}")
            return None

    async def send_transaction(self, transaction: Transaction, signer: Any, opts: TxOpts = TxOpts()) -> Optional[str]:
        """
        Sends a transaction to the Solana network.
        """
        try:
            response = await self.client.send_transaction(transaction, signer, opts=opts)
            logger.info(f"Transaction sent: {response['result']}")
            return response['result']
        except Exception as e:
            logger.error(f"Error sending transaction: {e}")
            return None

    async def close(self) -> None:
        """
        Closes the connection to the Solana RPC client.
        """
        await self.client.close()
        logger.info("Solana RPC connection closed")
