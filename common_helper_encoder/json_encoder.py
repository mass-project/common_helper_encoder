import json
import datetime
from base64 import standard_b64encode


class ReportEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, bytes):
            return standard_b64encode(obj).decode('utf-8')
        return json.JSONEncoder.default(self, obj)
