import random

class RandomizedSet:

    def __init__(self):
        self.val_idx_mapping = dict()
        self.vals = []
        

    def insert(self, val: int) -> bool:
        is_before_absent = val not in self.val_idx_mapping
        if is_before_absent:
            self.val_idx_mapping[val] = len(self.vals)
            self.vals.append(val)

        return is_before_absent
        

    def remove(self, val: int) -> bool:
        is_before_present = val in self.val_idx_mapping
        if is_before_present:
            idx = self.val_idx_mapping[val]
            last_val = self.vals[-1]
            self.vals[idx] = last_val
            self.vals.pop()
            self.val_idx_mapping[last_val] = idx

            del self.val_idx_mapping[val]

        return is_before_present
        

    def getRandom(self) -> int:
        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()