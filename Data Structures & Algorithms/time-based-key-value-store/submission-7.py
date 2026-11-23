from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if key in self.time_map:
            stored_val, stored_ts = "", 0
            for val, ts in self.time_map[key]:
                # print(f"val: {val} | ts: {ts} | timstamp: {timestamp}")
                if ts > timestamp:
                    # print("HIT")
                    break
                stored_val, stored_ts = val, ts
            return stored_val

        return ""
