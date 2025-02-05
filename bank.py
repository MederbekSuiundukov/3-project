class Amount:
    def __init__(self, amount: float, timestamp: datetime, transaction_type: str):
        self.amount = amount
        self.timestamp = timestamp
        self.transaction_type = transaction_type
    def __str__(self):
        return f"{self.timestamp} - {self.transaction_type}: $ {self.amount: .2f}"
