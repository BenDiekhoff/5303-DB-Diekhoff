# import redisCluster

# startup_nodes = [{"host": "localhost", "port": "7000"}]

# #  {"host": "localhost", "port": "7001"},
# #     {"host": "localhost", "port": "7002"}

# rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)

# rc.set("foo", "bar")
# print(rc.get("foo"))



# rm0 = redis.Redis(host='localhost', port=7000, db=0)
# rm1 = redis.Redis(host='localhost', port=7001, db=0)
# rm2 = redis.Redis(host='localhost', port=7002, db=0)
# rs0 = redis.Redis(host='localhost', port=7004, db=0)
# rs1 = redis.Redis(host='localhost', port=7005, db=0)
# rs2 = redis.Redis(host='localhost', port=7003, db=0)