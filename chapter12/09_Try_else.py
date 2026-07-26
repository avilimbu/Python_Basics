try:
    balance = 5000
    amount = int(input("Enter the amount to withdraw: "))

    if amount > balance:
        raise ValueError("Insufficient balance")

    remaining_balance = balance - amount

except ValueError as e:
    print(f"Error: {e}")

else:
    print(f"Withdrawal successful!")
    print(f"Remaining balance: ${remaining_balance}")

