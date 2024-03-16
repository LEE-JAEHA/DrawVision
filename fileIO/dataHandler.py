import pickle

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def save_data(self, data):
        with open(self.file_path, 'wb') as file:
            pickle.dump(data, file)
        print(f"데이터가 {self.file_path}에 저장되었습니다.")
    
    def load_data(self):
        try:
            with open(self.file_path, 'rb') as file:
                data = pickle.load(file)
            print(f"데이터가 {self.file_path}에서 로드되었습니다.")
            return data
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")
            return None

if __name__ == "__main__":
    list_handler = DataHandler("list_data.pkl")
    data_list = [1, 2, 3, 4, 5]
    list_handler.save_data(data_list)
    loaded_list = list_handler.load_data()
    print("로드된 리스트 데이터:", loaded_list)
    
    # 딕셔너리 데이터 저장 및 로드
    dict_handler = DataHandler("dict_data.pkl")
    data_dict = {"name": "John", "age": 30, "city": "New York"}
    dict_handler.save_data(data_dict)
    loaded_dict = dict_handler.load_data()
    print("로드된 딕셔너리 데이터:", loaded_dict)
