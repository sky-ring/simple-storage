from rift import *
from rift.wallet.wallet_manager import WalletManager
from contracts.storage import Storage


def deploy(network: Network):
    # Get our wallet and it's address
    wallet = WalletManager.acquire_wallet(network)
    my_addr = wallet.calculate_address()
    # Create initial data for contract
    init_data = Storage.Data(admin=my_addr, value=0).as_cell()
    # Create a change body as the first message to the contract
    body = Storage.ChangeBody(new_value=1)
    # Send the deploy request
    msg, addr = Storage.deploy(init_data, amount=1 * 10**8, body=body.as_cell())
    print("Contract getting deployed to:", MsgAddress.human_readable(addr))
    return msg, False
