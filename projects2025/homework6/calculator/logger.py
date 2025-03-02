"""Logging configuration for calculator"""
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create logger
logger = logging.getLogger("calculator")

# Set log level from environment variable
log_level_str = os.getenv("CALCULATOR_LOG_LEVEL", "INFO")
log_level = getattr(logging, log_level_str.upper(), logging.INFO)

# Configure logger
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(log_level)

# File handler for DEBUG and above
file_handler = logging.FileHandler("calculator.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)