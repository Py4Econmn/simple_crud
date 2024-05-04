from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order

class IBAPIClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)

class IBWrapper(EWrapper):
    def __init__(self):
        EWrapper.__init__(self)

    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)
        self.nextValidOrderId = orderId

def place_order():
    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"

    order = Order()
    order.action = "BUY"
    order.totalQuantity = 100  # Change quantity as needed
    order.orderType = "MKT"  # Market order
    order.transmit = True

    app.placeOrder(app.nextValidOrderId, contract, order)

# Connect to TWS or IB Gateway
app = IBAPIClient(IBWrapper())
app.connect("127.0.0.1", 7497, clientId=0)  # Use correct IP and port

# Place the order
place_order()

# Disconnect from IB
app.disconnect()






def main():
    # Your credentials
    account_id = "YOUR_ACCOUNT_ID"
    username = "YOUR_USERNAME"
    password = "YOUR_PASSWORD"
    
    # Connect to TWS or IB Gateway
    app = IBAPIClient(IBWrapper())
    app.connect("127.0.0.1", 7497, clientId=0)  # Use correct IP and port

    # Authenticate
    app.reqIds(-1)  # Request the next valid order ID
    app.run()

    # Place the order (you may want to place it within the authentication callback)
    place_order(app, account_id)

    # Disconnect from IB
    app.disconnect()

def place_order(app, account_id):
    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"

    order = Order()
    order.action = "BUY"
    order.totalQuantity = 100  # Change quantity as needed
    order.orderType = "MKT"  # Market order
    order.transmit = True
    order.account = account_id  # Set your account ID here

    app.placeOrder(app.nextValidOrderId, contract, order)

if __name__ == "__main__":
    main()





def main():
    # Demo account credentials
    account_id = "YOUR_DEMO_ACCOUNT_ID"
    username = "YOUR_DEMO_USERNAME"
    password = "YOUR_DEMO_PASSWORD"
    
    # Connect to the Paper Trading environment
    app = IBAPIClient(IBWrapper())
    app.connect("paperaccount.ibkr.com", 7497, clientId=0)  # Use correct host and port for paper trading

    # Authenticate
    app.reqIds(-1)  # Request the next valid order ID
    app.run()

    # Place the order
    place_order(app, account_id)

    # Disconnect from IB
    app.disconnect()

def place_order(app, account_id):
    # Define contract and order
    # Place order as usual

if __name__ == "__main__":
    main()
