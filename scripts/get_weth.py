from scripts.helpful_scripts import get_account
from brownie import config, network, interface


def main():
    get_weth()


def get_weth():
    account = get_account()
    weth = interface.WethInterface(
        config["networks"][network.show_active()]["weth_token"]
    )
    tx = weth.deposit({"from": account, "value": 0.01 * 10**18})
    tx.wait(1)
    print("Received 0.1 WETH")
