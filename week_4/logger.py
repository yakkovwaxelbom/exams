import json
import time
import functools
import os

class Logger:
    def __init__(self, path):
        os.makedirs(path, exist_ok=True)

        self.path = path
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.data = {d["url"]: d for d in json.load(f)}
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {}

    def _save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(list(self.data.values()), f, indent=4, ensure_ascii=False)

        self.summary()

    def log_call(self, url, method):
        def decorator(func):
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                start = time.time()

                import inspect
                if inspect.iscoroutinefunction(func):
                    result = func(*args, **kwargs)
                else:
                    result = func(*args, **kwargs)

                duration = time.time() - start

                entry = self.data.get(url)
                if not entry:
                    entry = {
                        "url": url,
                        "method": method,
                        "stats": {"total_requests_received": 0, "avg_handling_time": 0}
                    }
                    self.data[url] = entry

                stats = entry["stats"]
                total_calls = stats["total_requests_received"]
                avg_time = stats['avg_handling_time']

                stats["total_requests_received"] += 1
                stats["avg_handling_time"] = (avg_time * total_calls + duration) / (total_calls + 1)

                self._save()
                return result

            return wrapper

        return decorator

    def summary(self, path="data/summary.json"):
        os.makedirs(path, exist_ok=True)

        if not self.data:
            print("No data to summarize.")
            return

        highest_requests = max(
            self.data.values(), key=lambda x: x["stats"]["total_requests_received"]
        )
        lowest_requests = min(
            self.data.values(), key=lambda x: x["stats"]["total_requests_received"]
        )

        highest_handling_time = max(
            self.data.values(), key=lambda x: x["stats"]["avg_handling_time"]
        )
        lowest_handling_time = min(
            self.data.values(), key=lambda x: x["stats"]["avg_handling_time"]
        )

        summary_data = {
            "highest_requests": {
                "name": f"{highest_requests['url']} {highest_requests['method']}",
                "number": highest_requests["stats"]["total_requests_received"]
            },
            "lowest_requests": {
                "name": f"{lowest_requests['url']} {lowest_requests['method']}",
                "number": lowest_requests["stats"]["total_requests_received"]
            },
            "highest_handeling_time": {
                "name": f"{highest_handling_time['url']} {highest_handling_time['method']}",
                "number": round(highest_handling_time["stats"]["avg_handling_time"], 2)
            },
            "lowest": {
                "name": f"{lowest_handling_time['url']} {lowest_handling_time['method']}",
                "number": round(lowest_handling_time["stats"]["avg_handling_time"], 2)
            }
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(summary_data, f, indent=4, ensure_ascii=False)


logger = Logger("data/endpoints.json")
