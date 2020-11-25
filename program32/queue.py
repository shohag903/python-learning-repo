from collections import deque

bank = deque(["tanvir", "shohag", "bijoy"])
bank.popleft()
bank.popleft()
bank.popleft()
print(bank)

if not bank:
    print("no person left")