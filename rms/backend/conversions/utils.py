from typing import List, Dict

from fuzzywuzzy import fuzz, process


def extract_proposals(values: List, fuzzywuzzy_proposals: List, num_picks=1) -> Dict:
    # TODO: What happens if more than one top proposal?

    mapping_proposal = {}
    for i, val in enumerate(values):
        cands = fuzzywuzzy_proposals[i]
        if len(cands) == 0:
            mapping_proposal[val] = []
        elif len(cands) < num_picks:
            mapping_proposal[val] = [{'value': c[0], 'match': c[1]} for c in cands]
        else:
            mapping_proposal[val] = [{'value': c[0], 'match': c[1]} for c in cands[:num_picks]]

    return mapping_proposal


def process_fuzzywuzzy(string: str, search_set: List):
    try:
        return process.extract(string, search_set, scorer=fuzz.ratio)
    except TypeError:
        return []


def prune_zip4(zipcode: str) -> str:
    if '-' in zipcode:
        zipcode = zipcode.split('-')[0].rstrip(' ')
        if len(zipcode) == 4:
            zipcode = '0' + zipcode
        return zipcode
    return zipcode
