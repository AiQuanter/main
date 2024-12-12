import os
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # API Keys
    twitter_bearer_token: str = Field(..., env="TWITTER_BEARER_TOKEN")
    reddit_client_id: str = Field(..., env="REDDIT_CLIENT_ID")
    reddit_client_secret: str = Field(..., env="REDDIT_CLIENT_SECRET")

    # Solana Configuration
    solana_rpc_url: str = Field("https://api.mainnet-beta.solana.com", env="SOLANA_RPC_URL")
    smart_contract_program_id: str = Field(..., env="SMART_CONTRACT_PROGRAM_ID")

    # Logging
    log_level: str = Field("INFO", env="LOG_LEVEL")

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
