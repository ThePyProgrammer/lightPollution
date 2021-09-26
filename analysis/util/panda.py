import pandas as pd
import requests

def read_csv(loc, *args, **kwargs):
    if re.search(r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)", loc):
        return read_csv(requests.get(loc, allow_redirects=True).content, *args, **kwargs)
    loc = loc.strip("\n")
    if re.search(r"[\n:<>\"/\|?*]", loc):
        return pd.read_csv(StringIO(loc), *args, **kwargs)
    else:
        return pd.read_csv(loc, *args, **kwargs)