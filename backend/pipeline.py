import pandas as pd
from fastapi.logger import logger

from config import settings


def gather_canotify_data():
    try:
        df_cases = pd.read_csv(settings.URL_CASES_DEATHS)
        df_cases.to_csv(
            settings.OUTPUT_DATA / ("cases.csv"),
            index=False,
        )
        logger.info("Data gathering OK")
    except Exception as e:
        logger.error("Data gathering ERROR")
        logger.error(str(e))
