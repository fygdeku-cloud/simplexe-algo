class Account:
    def __init__(self, owner, initial_balance=0.0):
        self.owner = owner
        self._balance = initial_balance  # Protected attribute (Encapsulation)

    def deposit(self, amount):
        """Deposits money into the account if the amount is positive."""
        if amount > 0:
            self._balance += amount
            print(f"[Deposit] {amount} added to {self.owner}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws money if funds are sufficient and prevents negative balance."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self._balance:
            print(f"[Error] Withdrawal denied for {self.owner}: Insufficient funds. (Current balance: {self._balance})")
        else:
            self._balance -= amount
            print(f"[Withdrawal] {amount} withdrawn from {self.owner}'s account.")

    def get_balance(self):
        """Getter to safely access the protected balance."""
        return self._balance


class SavingsAccount(Account):  # Inheritance from Account
    def __init__(self, owner, initial_balance=0.0, interest_rate=0.02):
        # Call the parent class constructor
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Applies interest rate to the current balance."""
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"[Interest] Applied {self.interest_rate * 100}% interest. {interest} added to {self.owner}'s account.")


# --- Main Script Execution ---
if __name__ == "__main__":
    print("--- Testing Standard Account ---")
    alice_acc = Account("Alice", 500)
    alice_acc.deposit(200)
    alice_acc.withdraw(100)
    alice_acc.withdraw(1000)  # Should fail
    print(f"Alice's Final Balance: {alice_acc.get_balance()}\n")

    print("--- Testing Savings Account ---")
    bob_savings = SavingsAccount("Bob", 1000, interest_rate=0.05)
    bob_savings.deposit(500)
    bob_savings.apply_interest()  # Should add 5% to 1500 -> 75
    bob_savings.withdraw(200)
    print(f"Bob's Final Balance: {bob_savings.get_balance()}")


