from collections import defaultdict

class StockSummary:
    def __init__(self):
        self.stock_symbol = None
        self.stock_name = None
        self.stock_mean_value_per_date = defaultdict(float)
        self.stock_mean_volume_per_date = defaultdict(float)
        self.stock_mean_value_per_year = defaultdict(float)

if __name__ == "__main__":
    stock_summary = StockSummary(stock_symbol="abc")
    print(stock_summary)
