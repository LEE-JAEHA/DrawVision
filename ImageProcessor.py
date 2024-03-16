import cv2

class ImageProcessor:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise ValueError("이미지를 읽을 수 없습니다.")
    
    def add_bounding_box(self, x_min, y_min, x_max, y_max, color=(0, 255, 0), thickness=2):
        cv2.rectangle(self.image, (x_min, y_min), (x_max, y_max), color, thickness)
    
    def add_bounding_boxes(self, boxes, color=(0, 255, 0), thickness=2):
        for box in boxes:
            x_min, y_min, x_max, y_max = box
            self.add_bounding_box(x_min, y_min, x_max, y_max, color, thickness)
    
    def add_text(self, text, x, y, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(255, 255, 255), thickness=2):
        cv2.putText(self.image, text, (x, y), font, font_scale, color, thickness)
    
    def save_image(self, output_path):
        cv2.imwrite(output_path, self.image)
        print(f"이미지가 {output_path}에 저장되었습니다.")


