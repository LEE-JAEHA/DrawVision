from img_module.ImageProcessor import ImageProcessor
from img_module.evaluation_2D import BoundingBox, HungarianMatcher
import numpy as np
if __name__ == "__main__":
    image_processor = ImageProcessor("/Users/jaeha/Desktop/jaeha/son2.png")

    predicted_boxes = [BoundingBox(10, 10, 50, 50), BoundingBox(40, 20, 60, 60), BoundingBox(100, 30, 70, 70)]
    true_boxes = [BoundingBox(15, 15, 55, 55), BoundingBox(25, 25, 65, 65), BoundingBox(80, 80, 120, 120)]

    for idx,pb in enumerate(predicted_boxes):
        image_processor.add_bounding_box_with_comment(pb.x1,pb.y1,pb.x2,pb.y2,comment=str(idx),thickness=1)
    for idx,tb in enumerate(true_boxes):
        image_processor.add_bounding_box_with_comment(tb.x1,tb.y1,tb.x2,tb.y2,comment=str(idx),color=(0,0,255),thickness=1)
    # image_processor.add_text("Example Text", 50, 50)
    image_processor.save_image("./output_image.jpg")
    matcher = HungarianMatcher(predicted_boxes, true_boxes)
    matched_indices = matcher.match_boxes()

    # 결과 출력
    print("Matched Indices:", matched_indices)
