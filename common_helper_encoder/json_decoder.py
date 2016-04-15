import json

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(value, datetime.datetime):
            return value.isoformat()
        return json.JSONEncoder.default(self,obj)
