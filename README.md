# 图片创建日期水印工具 📷

一个简单易用的命令行工具，用于为图片添加文件创建日期水印。

## 功能特点 ✨

- 🎯 自动读取图片文件的创建日期
- 🎨 支持自定义水印颜色、大小和位置
- 📁 批量处理整个目录的图片
- 🖼️ 支持多种图片格式（JPG、PNG、BMP等）
- 📂 自动创建输出目录

## 安装依赖 🔧

```bash
pip install Pillow
```
使用方法 🚀
基本用法
bash
## 处理单张图片
```bash
python watermark.py photo.jpg
```

## 处理整个目录
```bash
python watermark.py /path/to/photos/
```


## 自定义字体大小
```bash
python watermark.py photos/ --font-size 50
```

## 自定义水印颜色
```bash
python watermark.py photos/ --color blue
```

## 自定义水印位置
```bash
python watermark.py photos/ --position top-left
```

## 组合使用所有选项
```bash
python watermark.py photos/ --font-size 60 --color red --position center
```
## 参数说明 ⚙️
### 水印颜色
white - 白色（默认）

black - 黑色

red - 红色

blue - 蓝色

green - 绿色

### 水印位置
top-left - 左上角

top-right - 右上角

center - 居中

bottom-left - 左下角

bottom-right - 右下角（默认）

### 字体大小
默认值：40

建议范围：20-100

### 输出说明 📂
处理后的图片将保存在新的子目录中：

```text
原目录/
├── image1.jpg
├── image2.jpg
└── 原目录_watermark/      # 自动创建的输出目录
    ├── wm_image1.jpg     # 带水印的图片
    └── wm_image2.jpg
```
### 支持的图片格式 📷
--JPEG (.jpg, .jpeg)

--PNG (.png)

--BMP (.bmp)

--其他Pillow支持的格式