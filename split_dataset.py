from pathlib import Path
import random
import shutil

base = Path("dataset")
images_train = base / "images" / "train"
images_val = base / "images" / "val"
labels_train = base / "labels" / "train"
labels_val = base / "labels" / "val"

images_val.mkdir(parents=True, exist_ok=True)
labels_val.mkdir(parents=True, exist_ok=True)

extensions = {".jpg", ".jpeg", ".png"}
images = [p for p in images_train.iterdir()
          if p.suffix.lower() in extensions]

random.seed(42)
random.shuffle(images)

count = int(len(images) * 0.2)
selected = images[:count]

for img in selected:
    label = labels_train / (img.stem + ".txt")

    shutil.move(str(img), str(images_val / img.name))

    if label.exists():
        shutil.move(str(label), str(labels_val / label.name))

print("Validation images:", len(selected))
print("Validation labels:", len(list(labels_val.glob("*.txt"))))
print("Remaining training images:", len(list(images_train.iterdir())))