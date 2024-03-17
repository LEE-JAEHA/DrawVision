from img_module.ImageProcessor import ImageProcessor
import numpy as np
if __name__ == "__main__":
    image_processor = ImageProcessor("/Users/jaeha/Desktop/jaeha/son2.png")
    bounding_boxes = [(100, 100, 300, 300), (200, 200, 400, 400)]  # 여러 개의 bounding box 좌표 리스트
    
    np.random.seed(0)
    points = np.random.rand(30, 2) * 100  # 30개의 랜덤한 (x, y) 좌표 생성 (이 예시에서는 400x400 이미지 내에서 생성)
    image_processor.draw_convex_hull(points)
    # image_processor.add_bounding_boxes(bounding_boxes)
    # image_processor.add_text("Example Text", 50, 50)
    image_processor.save_image("./output_image.jpg")