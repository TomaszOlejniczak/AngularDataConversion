import logging
from typing import Dict

from fuzzywuzzy import fuzz, process

from rms.backend.conversions.data import COLUMN_CONVERSIONS

logger = logging.getLogger(__name__)


def propose_column_mapping(column_name: str) -> Dict:
    proposals = {}
    for item in list(COLUMN_CONVERSIONS.keys()):
        proposal = process.extract(column_name, list(COLUMN_CONVERSIONS.get(item, [])), scorer=fuzz.ratio)
        proposals.update({item: proposal})

    best = max(list(proposals.keys()), key=lambda x: max(list(zip(*proposals.get(x, [])))[1]))
    logger.info(f'Best proposal for columne {column_name}: '
                f'{max(proposals.get(best, []), key=lambda x: x[1])}')
    return {column_name: best}
