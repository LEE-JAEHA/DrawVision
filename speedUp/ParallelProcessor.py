import multiprocessing
from functools import partial

class ParallelProcessor:
    def __init__(self, num_processes=None):
        if num_processes is None:
            self.num_processes = multiprocessing.cpu_count()
        else:
            self.num_processes = num_processes
    
    def process_task(self, task_function, data_list):
        with multiprocessing.Pool(processes=self.num_processes) as pool:
            results = pool.starmap(task_function, data_list)
        
        return results

# 예시 작업 함수
def print_add_three_numbers(text, a, b, c):
    print(text)
    return a, b, c

# 사용 예시
if __name__ == "__main__":
    data = [("First set:", 1, 2, 3), ("Second set:", 4, 5, 6), ("Third set:", 7, 8, 9)]  # 작업할 데이터 리스트
    processor = ParallelProcessor(num_processes=4)  # 병렬 처리 객체 생성
    
    # 데이터를 병렬로 출력하고 반환하기
    results = processor.process_task(partial(print_add_three_numbers), data)
    
    print("Results:", results)
