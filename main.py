from ImageProcessor import ImageProcessor

if __name__ == "__main__":
    image_processor = ImageProcessor("input_image.jpg")
    bounding_boxes = [(100, 100, 300, 300), (200, 200, 400, 400)]  # 여러 개의 bounding box 좌표 리스트
    image_processor.add_bounding_boxes(bounding_boxes)
    image_processor.add_text("Example Text", 50, 50)
    image_processor.save_image("output_image.jpg")