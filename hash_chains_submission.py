# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            values = self.elems.get(query.ind)
            if values:
                self.write_chain(reversed(values))
            else:
                self.write_chain([])
        else:
            if query.type == 'find':
                wasFound = False
                values = self.elems.get(self._hash_func(query.s))
                if values:                                    
                    for value in values:
                        if value == query.s:
                            wasFound = True
                self.write_search_result(wasFound)                
            elif query.type == 'add':
                values = self.elems.get(self._hash_func(query.s))
                if values:
                    exists = False
                    for value in values:
                        if value == query.s:
                            exists = True
                    if not exists:
                        values.append(query.s)
                else:
                    values = [query.s]
                self.elems[self._hash_func(query.s)] = values                
            elif query.type == 'del':
                values = self.elems.get(self._hash_func(query.s))
                if values:
                    for idx, value in enumerate(values):
                        if value == query.s:
                            del values[idx]

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
