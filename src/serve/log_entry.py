from __future__ import annotations

import json

from datetime import datetime, timezone
from pathlib import Path
from serialize import JSONDict


class LogEntry:
    def __init__(self, logs_dir: Path, log_entry_json: JSONDict):
        self.logs_dir = logs_dir
        self.json = log_entry_json

        creation_timestamp = self.json['creation_timestamp']
        self.log_id = self.json['log_id']
        self.log_message = self.json['log_message']

        created_datetime = datetime.fromtimestamp(
            creation_timestamp, tz=timezone.utc
        )
        created = created_datetime.isoformat(sep=' ', timespec='seconds')
        self.json['created'] = created

        filename = f'{self.log_id:05d} {created}.json'.replace(' ', '_')
        self.path = self.logs_dir / filename

    @classmethod
    def get_entries(cls, logs_dir: Path, log_body: bytes) -> list[LogEntry]:
        body_text = log_body.decode('utf-8')
        body_json = json.loads(body_text)
        log = body_json['log']
        logs_array = log['logs_array']
        return [
            LogEntry(logs_dir, log_entry_json) for log_entry_json in logs_array
        ]

    def write(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.json, f, indent=4, sort_keys=True)
