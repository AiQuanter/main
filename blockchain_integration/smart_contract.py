import logging
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, Transaction
from solana.rpc.async_api import AsyncClient
from solana.rpc.types import TxOpts
from typing import Any, Optional, Dict

logger = logging.getLogger(__name__)

class SmartContract:
    def __init__(self, program_id: str, rpc_url: str = "https://api.mainnet-beta.solana.com"):
        """
        Initializes the SmartContract class to interact with Solana blockchain smart contracts.
        """
        self.program_id = PublicKey(program_id)
        self.client = AsyncClient(rpc_url)
        logger.info(f"SmartContract initialized with program ID {program_id}")

    async def invoke_contract(self, params: Dict[str, Any], signer: Any) -> Optional[str]:
        """
        Invokes a smart contract function with the provided parameters.
        """
        try:
            # Example of creating a transaction instruction
            instruction = TransactionInstruction(
                keys=[],
                program_id=self.program_id,
                data=b'',  # Add data for the instruction if needed
            )
            transaction = Transaction().add(instruction)
            response = await self.client.send_transaction(transaction, signer, opts=TxOpts(skip_confirmation=False))
            logger.info(f"Smart contract invoked: {response['result']}")
            return response['result']
        except Exception as e:
            logger.error(f"Error invoking smart contract: {e}")
            return None

    async def close(self) -> None:
        """
        Closes the connection to the Solana RPC client.
        """
        await self.client.close()
        logger.info("SmartContract RPC connection closed")
