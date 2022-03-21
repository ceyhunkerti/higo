from typing import List
import sugarcrm

import sugarcrm

url = "https://suitecrmdemo.dtbc.eu/service/v2/rest.php"
session = sugarcrm.Session(url, "Demo", "Demo")


def get_leads(
    fields: List[str], offset: int = 0, max_results: int = 0
) -> List[sugarcrm.Lead]:
    query = sugarcrm.Lead()
    results = session.get_entry_list(
        query,
        fields=fields,
        offset=offset,
        max_results=max_results,
    )
    return results
