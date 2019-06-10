import json

class Account():
    def __init__(self):
        self.server = ''
        self.server_port = 0
        self.password = ''
        self.method = ''
        self.remarks = ''
        self.timeout = 5

    def get_account(self):
        account = {
            "server": self.server,
            "server_port": self.server_port,
            "password": self.password,
            "method": self.method,
            "remarks": self.remarks,
            "timeout": self.timeout
        }
        return account

with open('tmp', 'r') as f:
    data = f.read().split('\n')

account_list = []
index = 1
for line in data:
    print(index)
    index += 1
    line = line.strip().split('\t')
    print(line)
    account = Account()
    account.server = line[1].strip()
    account.server_port = int(line[2].strip())
    account.password = line[4].strip()
    account.method = line[3].strip()

    # print(account.get_account())
    account_list.append(account.get_account())
print(account_list)

config = {"configs":account_list}

print(config)

with open('gui-config.json', 'w') as f:
    ss_json = json.dumps(config)
    f.write(ss_json)




    