import multiprocessing

class ParallelProcessor:
    def __init__(self, num_processes=None):
        if num_processes is None:
            self.num_processes = multiprocessing.cpu_count()
        else:
            self.num_processes = num_processes
    
    def process_task(self, task_function, data_list):
        chunk_size = len(data_list) // self.num_processes
        chunks = [data_list[i:i+chunk_size] for i in range(0, len(data_list), chunk_size)]
        
        with multiprocessing.Pool(processes=self.num_processes) as pool:
            results = pool.map(task_function, chunks)
        
        return results

# 예시 작업 함수
def square_numbers(numbers):
    return [x * x for x in numbers]

# 사용 예시
if __name__ == "__main__":
    data = list(range(1, 11))  # 작업할 데이터 리스트
    processor = ParallelProcessor(num_processes=4)  # 병렬 처리 객체 생성
    
    # 데이터를 병렬로 제곱하기
    squared_results = processor.process_task(square_numbers, data)
    
    print("Squared Results:", squared_results)
