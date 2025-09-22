#!/usr/bin/env python3
"""
图片创建日期水印工具 - Vibe Coding 风格
快速实现，让功能先跑起来！
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont
import argparse
from pathlib import Path
from datetime import datetime


def get_file_date(file_path):
    """vibe方式获取文件日期 - 快速简单实现"""
    try:
        # 获取文件状态，优先使用创建时间，没有就用修改时间
        stat = os.stat(file_path)

        # 简单粗暴的日期获取：有创建时间用创建时间，没有用修改时间
        if hasattr(stat, 'st_birthtime'):
            timestamp = stat.st_birthtime  # macOS
        else:
            timestamp = stat.st_ctime if os.name == 'nt' else stat.st_mtime  # Windows用ctime，Linux用mtime

        # 转换成漂亮日期格式
        file_date = datetime.fromtimestamp(timestamp)
        return file_date.strftime("%Y-%m-%d")

    except Exception as e:
        print(f"⚠️  获取 {file_path} 日期时出错: {e}")
        return "未知日期"


def add_watermark(image_path, output_path, watermark_text, font_size=40, color="white", position="bottom-right"):
    """核心水印功能 - vibe风格快速实现"""
    try:
        # 打开图片
        img = Image.open(image_path).convert('RGBA')

        # 创建水印图层
        watermark_layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark_layer)

        # vibe字体方案：先试几个常见字体路径
        font = None
        font_paths = [
            "Arial.ttf",
            "/System/Library/Fonts/Arial.ttf",  # macOS
            "C:/Windows/Fonts/arial.ttf",  # Windows
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # Linux
        ]

        for path in font_paths:
            try:
                font = ImageFont.truetype(path, font_size)
                break
            except:
                continue

        # 如果都失败了，用默认字体
        if not font:
            font = ImageFont.load_default()
            print("📝 使用默认字体，效果可能一般")

        # 计算文字位置
        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        margin = 20  # 边距

        # 简单的位置映射
        if position == "top-left":
            x, y = margin, margin
        elif position == "top-right":
            x, y = img.width - text_width - margin, margin
        elif position == "center":
            x, y = (img.width - text_width) // 2, (img.height - text_height) // 2
        elif position == "bottom-left":
            x, y = margin, img.height - text_height - margin
        else:  # bottom-right
            x, y = img.width - text_width - margin, img.height - text_height - margin

        # 颜色处理
        color_map = {
            "white": (255, 255, 255, 200),
            "black": (0, 0, 0, 200),
            "red": (255, 0, 0, 200),
            "blue": (0, 0, 255, 200),
            "green": (0, 255, 0, 200)
        }

        rgba_color = color_map.get(color, color_map["white"])

        # 画个简单背景让文字更清晰
        draw.rectangle(
            [x - 5, y - 5, x + text_width + 5, y + text_height + 5],
            fill=(0, 0, 0, 100)
        )

        # 画文字
        draw.text((x, y), watermark_text, font=font, fill=rgba_color)

        # 合并保存
        result = Image.alpha_composite(img, watermark_layer)

        # 根据格式保存
        if image_path.lower().endswith('.png'):
            result.save(output_path)
        else:
            result.convert('RGB').save(output_path, quality=95)

        return True

    except Exception as e:
        print(f"❌ 处理 {image_path} 失败: {e}")
        return False


def process_images(input_path, font_size=40, color="white", position="bottom-right"):
    """处理图片的主函数 - vibe风格"""

    # 判断是文件还是目录
    if os.path.isfile(input_path):
        files = [Path(input_path)]
        input_dir = Path(input_path).parent
    else:
        input_dir = Path(input_path)
        # 支持的图片格式
        image_exts = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
        files = [f for f in input_dir.iterdir() if f.is_file() and f.suffix.lower() in image_exts]

    if not files:
        print("😅 没找到图片文件！")
        return

    # 创建输出目录
    output_dir = input_dir / f"{input_dir.name}_watermark"
    output_dir.mkdir(exist_ok=True)

    print(f"🎯 开始处理 {len(files)} 张图片...")
    print(f"📁 输出到: {output_dir}")

    success_count = 0

    for file_path in files:
        print(f"🔄 处理: {file_path.name}")

        # 获取文件日期
        file_date = get_file_date(file_path)
        watermark_text = file_date

        # 输出文件名
        output_file = output_dir / f"watermark_{file_path.name}"

        # 添加水印
        if add_watermark(str(file_path), str(output_file), watermark_text, font_size, color, position):
            print(f"✅ 完成: {output_file.name}")
            success_count += 1
        else:
            print(f"❌ 失败: {file_path.name}")

    print(f"\n🎉 处理完成！成功 {success_count}/{len(files)} 张图片")


def main():
    """主入口 - vibe风格简单直接"""
    parser = argparse.ArgumentParser(description='图片创建日期水印工具')
    parser.add_argument('path', help='图片文件或目录路径')
    parser.add_argument('--font-size', type=int, default=40, help='字体大小（默认40）')
    parser.add_argument('--color', default='white', choices=['white', 'black', 'red', 'blue', 'green'],
                        help='水印颜色（默认white）')
    parser.add_argument('--position', default='bottom-right',
                        choices=['top-left', 'top-right', 'center', 'bottom-left', 'bottom-right'],
                        help='水印位置（默认bottom-right）')

    args = parser.parse_args()

    # 简单验证
    if not os.path.exists(args.path):
        print("❌ 路径不存在！")
        return

    print("=" * 50)
    print("📷 图片创建日期水印工具")
    print("=" * 50)

    process_images(args.path, args.font_size, args.color, args.position)

    print("\n✨ 搞定！享受你的带水印图片吧！")


if __name__ == "__main__":
    main()