import nodecore_pop_api

host = 'http://127.0.0.1:8600'

# Create api object
api = nodecore_pop_api.nodecore_pop_api(host, True)

# Get current config
config = api.get_config()
print("GET /api/config")
print(config)

# Get miner info
miner_properties = api.get_miner_properties()
print("GET /api/miner")
print(miner_properties)

# Get operations
operations = api.get_operations()
print("GET /api/operations")
print(operations)

# Get last bitcoin block
lastbitcoinblock = api.get_lastbitcoinblock()
print("GET /api/lastbitcoinblock")
print(lastbitcoinblock)

# Quit NodeCore-PoP
# POST /api/quit
#quit = api.quit()

# Mine specific block number
# POST /api/mine
#mine = api.mine(413381)
#print("POST /api/mine")
#print(mine)

# Mine current block
#mine = api.mine_current_block()
#print("POST /api/mine")
#print(mine)

# Change config information example
#config = api.put_config('auto.mine.round1', 'true')
#print("PUT /api/config")
#print(config)
