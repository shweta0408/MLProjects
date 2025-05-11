import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Generate unique log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO
)

# Optionally, also log to console
console = logging.StreamHandler()
console.setFormatter(logging.Formatter(
    "[%(asctime)s] %(levelname)s - %(message)s"))
logging.getLogger().addHandler(console)

logger = logging.getLogger(__name__)
