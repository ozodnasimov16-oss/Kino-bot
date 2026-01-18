import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    # Bot
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    ADMIN_ID: int = int(os.getenv("ADMIN_ID", "0"))
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    
    # Channel
    CHANNEL_USERNAME: str = os.getenv("CHANNEL_USERNAME", "")
    MAX_CHANNELS: int = 5
    
    # Features
    ENABLE_STATISTICS: bool = True
    ENABLE_RATINGS: bool = True
    ENABLE_SEARCH: bool = True
    CACHE_TTL: int = 3600
    
    # Limits
    MAX_BROADCAST_RATE: float = 0.03
    MAX_MOVIE_SIZE_MB: int = 2000
    
    # Messages
    WELCOME_MESSAGE: str = "🎬 Xush kelibsiz! Premium kino botiga marhamat!"
    
    def __post_init__(self):
        """Validate and fix DATABASE_URL"""
        if not self.BOT_TOKEN:
            raise ValueError("BOT_TOKEN is required in .env file")
        if self.ADMIN_ID == 0:
            raise ValueError("ADMIN_ID is required in .env file")
        
        # Fix DATABASE_URL for asyncpg
        if self.DATABASE_URL:
            if self.DATABASE_URL.startswith("postgresql://"):
                self.DATABASE_URL = self.DATABASE_URL.replace(
                    "postgresql://", 
                    "postgresql+asyncpg://", 
                    1
                )
            elif self.DATABASE_URL.startswith("postgres://"):
                self.DATABASE_URL = self.DATABASE_URL.replace(
                    "postgres://", 
                    "postgresql+asyncpg://", 
                    1
                )

config = Config()
