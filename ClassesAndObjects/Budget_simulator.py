class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # ------------------------
    # Add money
    # ------------------------
    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    # ------------------------
    # Remove money
    # ------------------------
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    # ------------------------
    # Get current balance
    # ------------------------
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    # ------------------------
    # Transfer between categories
    # ------------------------
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    # ------------------------
    # Check if enough funds exist
    # ------------------------
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    # ------------------------
    # Print category nicely
    # ------------------------
    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        body = ""
        total = 0

        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            body += f"{desc:<23}{amt:>7}\n"
            total += item["amount"]

        return title + body + f"Total: {total:.2f}"


# -------------------------------------------------------
# Spending chart
# -------------------------------------------------------
def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    spent = []
    total_spent = 0

    for cat in categories:
        s = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                s += -item["amount"]
        spent.append(s)
        total_spent += s

    percentages = []
    for s in spent:
        p = int((s / total_spent) * 100)
        p = (p // 10) * 10
        percentages.append(p)

    # Draw bars
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for p in percentages:
            if p >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart
