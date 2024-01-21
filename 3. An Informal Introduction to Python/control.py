words = ['cat', 'window', 'dog']

for w in words:
    print(w, len(w))
    print(len(w))

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # Strategy:  Iterate over active copy
# for k, v in users.copy().items():
#     if v == 'inactive':
#         del users[k]


print(users)

# Strategy:  Create a new collection
active_users = {}
for k, v in users.items():
    if v == 'inactive':
        active_users[k] = v


print(active_users)
