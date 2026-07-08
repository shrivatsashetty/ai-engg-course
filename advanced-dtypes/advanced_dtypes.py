import arrow

# 1. Get current time (UTC or Local)
utc_now = arrow.utcnow()
local_now = arrow.now('US/Pacific')

print(f"Local Time Now: {local_now}")
print(f"UTC Time Now: {utc_now}")
