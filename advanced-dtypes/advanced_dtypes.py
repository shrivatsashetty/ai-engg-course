import arrow
from collections import namedtuple

# 1. Get current time (UTC or Local)
utc_now = arrow.utcnow()
ist_now = arrow.now("Asia/Kolkata")

print(f"Local Time Now: {ist_now}")
print(f"UTC Time Now: {utc_now}")

gmt_now = ist_now.to("Europe/London")

print(f"GMT Time Now: {gmt_now}")


user_profles = namedtuple("user_profiles", ["jhondoe", "janedoe"])

print(user_profles)