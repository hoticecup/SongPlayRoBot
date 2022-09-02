import os
API_ID = int(os.getenv("11743017"))
API_HASH = os.getenv("373553a5f244ebdf5fd63f66cedabb58")
BOT_TOKEN = os.getenv("5731688815:AAFiLM_Q8J4cNxD0r6OvEpZGIR1CZnpZsQE")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("1409869437", "").split()})
