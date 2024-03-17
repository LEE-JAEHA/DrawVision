import cv2
import numpy as np
class ImageProcessor:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise ValueError("이미지를 읽을 수 없습니다.")
    
    def add_bounding_box(self, x_min, y_min, x_max, y_max, color=(0, 255, 0), thickness=2):
        cv2.rectangle(self.image, (x_min, y_min), (x_max, y_max), color, thickness)
        
    def add_bounding_box_with_comment(self, x_min, y_min, x_max, y_max, comment="", color=(0, 255, 0), thickness=2):
            self.add_bounding_box(x_min, y_min, x_max, y_max, color, thickness)  # 기존 함수 호출
        if comment:
            self.add_text(comment, x_min, y_min - 5)  # 박스 위에 코멘트 추가
        
    def add_bounding_boxes(self, boxes, color=(0, 255, 0), thickness=2):
        for box in boxes:
            x_min, y_min, x_max, y_max = box
            self.add_bounding_box(x_min, y_min, x_max, y_max, color, thickness)
    
    def draw_convex_hull(self, points, color=(0, 255, 0), thickness=2):
        hull = cv2.convexHull(np.array(points).astype(np.int32))  # Convex Hull 계산
        cv2.polylines(self.image, [hull], isClosed=True, color=color, thickness=thickness)  # Convex Hull 그리기

    def draw_point(self, point, color=(0, 0, 255), radius=5):
        cv2.circle(self.image, (int(point[0]),int(point[1])), radius, color, -1)  # 점 그리기

    def draw_points(self, points, color=(0, 0, 255), radius=5):
        for point in points:
            self.draw_point(tuple(point), color, radius)  # 모든 점 그리기
    
    def add_text(self, text, x, y, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(255, 255, 255), thickness=2):
        cv2.putText(self.image, text, (x, y), font, font_scale, color, thickness)
    
    def save_image(self, output_path):
        cv2.imwrite(output_path, self.image)
        print(f"이미지가 {output_path}에 저장되었습니다.")


