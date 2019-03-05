# python3
import heapq
import random
import time

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)
     
    def read_data_test(self, num_workers, jobs):
        self.num_workers = num_workers
        self.jobs = jobs

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs_naive(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]
    
    def assign_jobs(self):
        self.start_times = [None] * len(self.jobs)
        self.assigned_workers = [None] * len(self.jobs)
        next_free_time = [(0, i) for i in range(self.num_workers)]
        
        for i in range(len(self.jobs)):
            start_time, index = heapq.heappop(next_free_time)
            self.start_times[i] = start_time
            self.assigned_workers[i] = index
            end_time = start_time + self.jobs[i]
            heapq.heappush(next_free_time, (end_time, index))                                    

    def solve(self):
        self.read_data()
        self.assign_jobs_naive()
        self.write_response()
    
    def solve_test(self, num_workers, jobs):
        self.read_data_test(num_workers, jobs)
        self.assign_jobs()
        return self.assigned_workers, self.start_times
        
        
    def solve_test_naive(self, num_workers, jobs):
        self.read_data_test(num_workers, jobs)
        self.assign_jobs_naive()
        return self.assigned_workers, self.start_times

def assert_correct(naive, queue):
    return naive == queue

if __name__ == '__main__':
    num_workers_one = 2
    jobs_one = [1, 2, 3, 4 ,5]
    job_queue_one = JobQueue()    
    print("Test Case One")
    assigned_workers_fast, start_times_fast = job_queue_one.solve_test(num_workers_one, jobs_one)
    assigned_workers, start_times = job_queue_one.solve_test_naive(num_workers_one, jobs_one)
    
    print(assert_correct((assigned_workers_fast, start_times_fast), (assigned_workers, start_times)))
    
    num_workers_two = 4
    jobs_two = [1 for i in range(20)]
    job_queue_two = JobQueue()    
    print("Test Case Two")
    assigned_workers_fast, start_times_fast = job_queue_two.solve_test(num_workers_two, jobs_two)
    assigned_workers, start_times = job_queue_two.solve_test_naive(num_workers_two, jobs_two)
    
    print(assert_correct((assigned_workers_fast, start_times_fast), (assigned_workers, start_times)))
    
    
    num_workers_three = 7
    jobs_three = [10, 9, 8, 7, 5, 6, 8, 10, 11, 5, 234, 5, 1, 1, 1, 1, 1, 1, 3, 14, 152, 25, 3, 6, 23, 5, 19, 1, 1, 3]
    job_queue_three = JobQueue()
    print("Test Case Three")
    assigned_workers_fast, start_times_fast = job_queue_two.solve_test(num_workers_two, jobs_two)
    assigned_workers, start_times = job_queue_two.solve_test_naive(num_workers_two, jobs_two)
    
    print(assert_correct((assigned_workers_fast, start_times_fast), (assigned_workers, start_times)))
    
    num_workers_rand = random.randint(1, 1000)
    jobs_rand = [random.randint(0, 1000000000) for _ in range(random.randint(5000, 10000))]
    job_queue_rand = JobQueue()
    print("Test Case Random")
    now = time.time()
    workers_heap, start_times_heap = job_queue_rand.solve_test(num_workers_rand, jobs_rand)
    end = time.time()
    print("Speed: " + str((end - now < 6)))
    
    workers, start_times = job_queue_rand.solve_test_naive(num_workers_rand, jobs_rand)
    print(assert_correct((workers_heap, start_times_heap), (workers, start_times)))