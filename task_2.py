total = 0.0

print("=" * 40)
print("   DecodeLabs Expense Tracker")
print("   Type 'quit' to finish & see total")
print("=" * 40)

while True:

    user_input = input("\nEnter expense amount: ")

    if user_input.lower() == "quit":
        break

    try:
        expense = float(user_input)

        if expense < 0:
            print("please enter the valid amount")
            continue

        total += expense
        print(f"  Added: Rs.{expense:.2f}  |  Running Total: Rs.{total:.2f}")

    except ValueError:
        print("  [!] Invalid data – please enter a number (e.g. 100, 50.5).")

print("\n" + "=" * 40)
print(f"   FINAL TOTAL SPENT: Rs.{total:.2f}")
print("=" * 40)