import numpy as np
from scipy.optimize import linear_sum_assignment

class BoundingBox:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate_iou(self, other):
        xA = max(self.x1, other.x1)
        yA = max(self.y1, other.y1)
        xB = min(self.x2, other.x2)
        yB = min(self.y2, other.y2)

        inter_area = max(0, xB - xA + 1) * max(0, yB - yA + 1)
        self_area = (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1)
        other_area = (other.x2 - other.x1 + 1) * (other.y2 - other.y1 + 1)

        iou = inter_area / float(self_area + other_area - inter_area)
        return iou

class HungarianMatcher:
    def __init__(self, predicted_boxes, true_boxes, threshold=0.9):
        self.predicted_boxes = predicted_boxes
        self.true_boxes = true_boxes
        self.threshold = threshold

    def match_boxes(self):
        num_pred_boxes = len(self.predicted_boxes)
        num_true_boxes = len(self.true_boxes)

        # IOU를 계산하여 cost matrix를 생성합니다.
        cost_matrix = np.zeros((num_pred_boxes, num_true_boxes))
        for i in range(num_pred_boxes):
            for j in range(num_true_boxes):
                cost_matrix[i, j] = 1 - self.predicted_boxes[i].calculate_iou(self.true_boxes[j])

        # 헝가리안 알고리즘을 사용하여 최적의 할당을 찾습니다.
        row_ind, col_ind = linear_sum_assignment(cost_matrix)

        matched_indices = [(row, col) for row, col in zip(row_ind, col_ind) if cost_matrix[row, col] <= self.threshold]

        return matched_indices

# # 예측된 bounding box와 실제 bounding box 리스트를 생성합니다.
# predicted_boxes = [BoundingBox(10, 10, 50, 50), BoundingBox(20, 20, 60, 60), BoundingBox(30, 30, 70, 70)]
# true_boxes = [BoundingBox(15, 15, 55, 55), BoundingBox(25, 25, 65, 65), BoundingBox(80, 80, 120, 120)]

# # 객체 생성 후 매칭 수행
# matcher = HungarianMatcher(predicted_boxes, true_boxes)
# matched_indices = matcher.match_boxes()

# # 결과 출력
# print("Matched Indices:", matched_indices)
