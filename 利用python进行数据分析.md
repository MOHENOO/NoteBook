# 利用python进行数据分析

时区统计(数据来自bit.ly的1.usa.gov)

```python
# %%
from collections import defaultdict
import json
path = 'usagov_bitly_data2013-05-17-1368832207.txt'

open(path).readline()
records = [json.loads(line) for line in open(path)]
records[0]
records[0]['tz']

# 对时区进行计数
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones[:10]


def get_counts(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

counts=get_counts(time_zones)
counts['America/New_York']
len(time_zones)

def top_counts(count_dict,n=10):
    value_key_pairs=[(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

top_counts(counts)

from collections import Counter
counts=Counter(time_zones)
counts.most_common(10)


#%%
```