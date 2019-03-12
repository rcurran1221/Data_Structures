# python3
import random
import time
import string
import os
import psutil

process = psutil.Process(os.getpid())

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
        self.elemsList = []
        self.results = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):        
        self.results.append('yes' if was_found else 'no')
        
    def write_chain(self, chain):
        self.results.append(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query_naive(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elemsList) if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elemsList.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elemsList.append(query.s)
            else:
                if ind != -1:
                    self.elemsList.pop(ind)
    
    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
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
                        

    def process_queries(self, queryCount, queries):
        for i in range(queryCount):
            self.process_query(Query(queries[i].split()))
        return self.results
    
    def process_queries_naive(self, queryCount, queries):
        for i in range(queryCount):
            self.process_query_naive(Query(queries[i].split()))
        return self.results    
    

def generate_random_query(stringLength, bucketCount):
    r = random.randint(0, 3)
    
    if r == 0:
        s = generate_random_string(stringLength)
        query = "add " + s
    if r == 1:
        s = generate_random_string(stringLength)
        query = "del " + s
    if r == 2:
        s = generate_random_string(stringLength)
        query = "find " + s
    if r == 3:
        i = random.randint(0, bucketCount -1)
        query = "check " + str(i)

    return query
    
def generate_random_string(length):
    s = ""
    for i in range(length):
        s = s + str(random.choice(string.ascii_letters))
    
    return s
        
if __name__ == '__main__':
    bucketsCount = 5
    queryCount = 12
    queries = ["add world", "add Hell0", "check 4", "find World", "find world", "del world", "check 4", "del Hell0", "add luck", "add GooD", "check 2", "del good"]
    
    proc = QueryProcessor(bucketsCount)
    procNaive = QueryProcessor(bucketsCount)
    results = proc.process_queries(queryCount, queries)
    resultsNaive = procNaive.process_queries_naive(queryCount, queries)
    print("Case 1 Correct: " + str(results == resultsNaive))
    
    
    bucketsCount = 4
    queryCount = 8
    queries = ["add test", "add test", "find test", "del test", "find test", "find Test", "add Test", "find Test"]
    
    proc = QueryProcessor(bucketsCount)
    procNaive = QueryProcessor(bucketsCount)
    results = proc.process_queries(queryCount, queries)
    resultsNaive = procNaive.process_queries_naive(queryCount, queries)
    print("Case 2 Correct: " + str(results == resultsNaive))
    
    
    bucketsCount = 3
    queryCount = 12
    queries = ["check 0", "find help", "add help", "add del", "add add", "find add", "find del", "del del", "find del", "check 0", "check 1", "check 2"]
    
    proc = QueryProcessor(bucketsCount)
    procNaive = QueryProcessor(bucketsCount)
    results = proc.process_queries(queryCount, queries)
    resultsNaive = procNaive.process_queries_naive(queryCount, queries)
    print("Case 3 Correct: " + str(results == resultsNaive))
    
    
    queryCount = 100000
    bucketsCount = random.randint(queryCount/5, queryCount)
    print("Buckets count: " + str(bucketsCount))
    gStart = time.time()
    queries = [generate_random_query(15, bucketsCount) for i in range(queryCount)]
    gEnd = time.time()
    print("Time to generate " + str(queryCount) + " queries: " + str(gEnd-gStart))
    
    proc = QueryProcessor(bucketsCount)
    start = time.time()
    results = proc.process_queries(queryCount, queries)
    end = time.time()
    print("Stress Test Timely: " + str(end - start < 7) + " " + str(end - start))
    memoryUsage = process.memory_info().rss * 1e-6
    print("Memory efficient: " + str(memoryUsage < 512) + " " + str(memoryUsage))
    
    procNaive = QueryProcessor(bucketsCount)
    resultsNaive = procNaive.process_queries_naive(queryCount, queries)
    print("Stress Test Correct: " + str(results == resultsNaive))
    
    
    
    
    
    
    
    
