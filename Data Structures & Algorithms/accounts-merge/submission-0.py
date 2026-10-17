# Helper class for easier Union Find
class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def union(self, n1, n2):
        root1, root2 = self.find(n1), self.find(n2)
        if root1 == root2:
            return False
        
        if self.rank[root1] == self.rank[root2]:
            self.parent[root2] = root1
            self.rank[root1] += 1
        elif self.rank[root2] > self.rank[root1]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1

        return True

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        uf = UnionFind(len(accounts))
        emailToAccIdx = {} # maps email -> account index

        # Becasue names of accounts can be repeated, we will use their indexes
        for idx, account in enumerate(accounts):
            # First value in the account array is the name so we want to skip that and go straight to the emails
            for email in account[1:]:
                if email in emailToAccIdx:
                    # If the email is already mapped to an account index we would want to merge the accounts togheter
                    uf.union(idx, emailToAccIdx[email])
                else:
                    emailToAccIdx[email] = idx

        # Each email should belong to a single account so we want to create these email accounts/groups
        # We want to take each index of the accounts and map it to it's list of emails
        emailGroups = defaultdict(list)
        for email, accountIdx in emailToAccIdx.items(): # index of account -> list of all emails
            repr = uf.find(accountIdx)
            emailGroups[repr].append(email)
        
        res = []
        for accountIdx, emails in emailGroups.items():
            # use the original accounts array to get the name of the account given it s index
            name = accounts[accountIdx][0]
            res.append([name] + sorted(emailGroups[accountIdx]))

        return res


