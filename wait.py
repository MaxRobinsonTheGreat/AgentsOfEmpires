"""
Wait for the tournament to finish. Polls Outputs/status.json.

Usage: python wait.py [poll_seconds] [stale_minutes]

Exits 0 and prints standings when tournament_done is true.
Exits 2 if the heartbeat goes stale (runner probably died).
Safe to re-run anytime; also safe to interrupt - status.json is the source of truth.
"""
import json
import sys
import time
from datetime import datetime

POLL = int(sys.argv[1]) if len(sys.argv) > 1 else 15
STALE_AFTER = int(sys.argv[2]) if len(sys.argv) > 2 else 10  # minutes

STATUS = "Outputs/status.json"

def load():
    with open(STATUS) as f:
        return json.load(f)

last_count = -1
while True:
    try:
        s = load()
    except (OSError, json.JSONDecodeError):
        print("status.json missing or unreadable, waiting...")
        time.sleep(POLL)
        continue

    n = len(s.get("games", []))
    if n != last_count:
        print("games completed: %d" % n)
        last_count = n

    if s.get("tournament_done"):
        print("TOURNAMENT DONE")
        print(json.dumps(s.get("standings", {}), indent=2))
        sys.exit(0)

    heartbeat = s.get("heartbeat")
    if heartbeat:
        age = (datetime.now() - datetime.fromisoformat(heartbeat)).total_seconds() / 60
        if age > STALE_AFTER:
            print("STALE: heartbeat is %.1f minutes old - runner probably died. Check Failures/ and runner logs." % age)
            sys.exit(2)

    time.sleep(POLL)
