# https://realpython.com/python-redis/#configuring-redis
import redis

r = redis.Redis(host='localhost', port=6379)
r.set("foo", "bar")
print(r.get("foo"))



# 127.0.0.1:6379> SET Bahamas Nassau
# OK
# 127.0.0.1:6379> SET Croatia Zagreb
# OK
# 127.0.0.1:6379> GET Croatia
# "Zagreb"
# 127.0.0.1:6379> GET Japan
# (nil)
capitals = {}
capitals["Bahamas"] = "Nassau"
capitals["Croatia"] = "Zagreb"
capitals.get("Croatia") #'Zagreb'
capitals.get("Japan") # None



#127.0.0.1:6379> MSET Lebanon Beirut Norway Oslo France Paris
#OK
#127.0.0.1:6379> MGET Lebanon Norway Bahamas
#1) "Beirut"
#2) "Oslo"
#3) "Nassau"
capitals.update({
"Lebanon": "Beirut",
"Norway": "Oslo",
"France": "Paris",
})
[capitals.get(k) for k in ("Lebanon", "Norway", "Bahamas")]
#['Beirut', 'Oslo', 'Nassau']


# 127.0.0.1:6379> EXISTS Norway
# (integer) 1
# 127.0.0.1:6379> EXISTS Sweden
# (integer) 0
"Norway" in capitals
#True
"Sweden" in capitals
#False


# 127.0.0.1:6379> HSET realpython url "https://realpython.com/"
# (integer) 1
# 127.0.0.1:6379> HSET realpython github realpython
# (integer) 1
# 127.0.0.1:6379> HSET realpython fullname "Real Python"
# (integer) 1
data = {
    "realpython": {
        "url": "https://realpython.com/",
        "github": "realpython",
        "fullname": "Real Python",
    }
}