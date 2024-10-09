import uuid
from loguru import logger

# Получение MAC-адреса устройства
def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    mac_address = ":".join([mac[e:e+2] for e in range(0, 12, 2)])
    logger.info("Reseiving MAC_ADR")
    return mac_address
