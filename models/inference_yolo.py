from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def load_model(model_path):
    return YOLO(model_path)

def detect_text(model, im_path):
    results = model(im_path, verbose=False)
    results = results[0].boxes
    return results

def visualize_bbox(im_path, results, conf_thres=0.7):
    im = Image.open(im_path)
    plt.imshow(im)
    plt.axis('off')
    for bbox in results:
        conf_score = bbox.conf.item()
        if conf_score < conf_thres:
            continue

        x1, y1, x2, y2 = bbox.xyxy[0].tolist()
        # label = bbox.cls.item()

        # Draw bounding box
        rect = patches.Rectangle(
            (x1, y1), x2 - x1, y2 - y1,
            linewidth=2, edgecolor='r', facecolor='none'
        )
        plt.gca().add_patch(rect)

        # Add confidence score
        text = f'{conf_score:.2f}'
        plt.text(x1 + 5, y1 - 10, text, color='k', fontsize=6, bbox=dict(facecolor='w', alpha=0.5))
    

if __name__ == '__main__':
    model_path = 'models/weights/yolo_best.pt'
    im_path = '/data/SceneTrialTrain/lfsosa_12.08.2002/IMG_2461.JPG'
    
    yolo_model = load_model(model_path)
    results = detect_text(yolo_model, im_path)
    visualize_bbox(im_path, results, conf_thres=0.7)
