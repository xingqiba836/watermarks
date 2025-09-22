## 使用方法：

```bash
# 安装依赖
pip install Pillow

# 给单张图片加水印
python watermark.py ~/Pictures/photo.jpg

# 给整个目录加水印，蓝色水印在左上角
python watermark.py ~/Pictures/vacation/ --color blue --position top-left

# 大号红色水印在中间
python watermark.py ./photos/ --font-size 60 --color red --position center