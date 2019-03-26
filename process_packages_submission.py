# python3

from collections import namedtuple
import heapq

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        if self.finish_time:
            while self.finish_time and self.finish_time[0] <= int(request.arrived_at):
                self.finish_time.pop(0)
            
        if self.size <= len(self.finish_time):
            return Response(True, -1)
        
        if self.finish_time:
            heapq.heappush(self.finish_time, self.finish_time[-1] + int(request.time_to_process))
        else:
            heapq.heappush(self.finish_time, int(request.arrived_at) + int(request.time_to_process))
        
        return Response(False, self.finish_time[-1] - int(request.time_to_process))


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)

def test(buffer_size, n_requests, packets):
    requests = []
    for i in range(n_requests):
        arrived_at, time_to_process = packets[i].split()
        requests.append(Request(arrived_at, time_to_process))
        
    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)
    
    for response in responses:
        print(response.started_at if not response.was_dropped else -1)

if __name__ == "__main__":
    main()
