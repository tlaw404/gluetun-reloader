import os
import time
import logging
import requests
from requests.auth import HTTPBasicAuth

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)

# Load config from environment
GLUETUN_URL = os.getenv("GLUETUN_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
INTERVAL_HOURS = float(os.getenv("INTERVAL_HOURS", "2"))

def stop_vpn():
    logging.info("Sending request to stop Gluetun VPN...")
    try:
        response = requests.put(
            GLUETUN_URL,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            headers={"Content-Type": "application/json"},
            json={"status": "stopped"}
        )
        if response.ok:
            logging.info(f"Success: {response.status_code} - {response.text}")
        else:
            logging.warning(f"Failed with status: {response.status_code} - {response.text}")
    except Exception as e:
        logging.error(f"Error while sending request: {e}")

if __name__ == "__main__":
    while True:
        stop_vpn()
        logging.info(f"Sleeping for {INTERVAL_HOURS} hours...")
        time.sleep(INTERVAL_HOURS * 3600)