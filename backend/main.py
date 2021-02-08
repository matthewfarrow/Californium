from web3 import Web3
import os

# ipcpath = os.path.join(os.path.expanduser('~'), '.local/share/trinity/ropsten/ipcs-eth1/jsonrpc.ipc')
# w3provider = Web3.IPCProvider(ipcpath)

projectId = 'eacb0a5460c944c7a0b3b0625e5259a1'
network = 'mainnet'
w3provider = Web3.HTTPProvider("https://"+network+".infura.io/v3/"+projectId)

w3 = Web3(w3provider)

