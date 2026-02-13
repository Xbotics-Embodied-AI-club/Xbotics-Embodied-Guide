#!/usr/bin/env python3
"""对扫描版 PDF 做 OCR，输出文本到 <主题>-ocr.txt。依赖：pymupdf、easyocr、Pillow（无需单独安装 Tesseract）。"""
import argparse
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("请先安装 PyMuPDF: pip install pymupdf", file=sys.stderr)
    sys.exit(1)
try:
    from PIL import Image
except ImportError:
    print("请先安装 Pillow: pip install Pillow", file=sys.stderr)
    sys.exit(1)


def pdf_page_to_image(fitz_page, dpi=200):
    """将一页 PDF 渲染为图像（高 dpi 利于 OCR）。"""
    mat = fitz.Matrix(dpi / 72, dpi / 72)
    pix = fitz_page.get_pixmap(matrix=mat, alpha=False)
    return Image.frombytes("RGB", [pix.width, pix.height], pix.samples)


def ocr_pdf(pdf_path: Path, out_path: Path, dpi: int = 200) -> int:
    import easyocr
    import numpy as np
    reader = easyocr.Reader(["ch_sim", "en"], gpu=False)
    doc = fitz.open(pdf_path)
    parts = []
    for i, page in enumerate(doc):
        img = pdf_page_to_image(page, dpi=dpi)
        arr = np.array(img)
        result = reader.readtext(arr)
        page_text = " ".join([item[1] for item in result])
        if page_text.strip():
            parts.append(page_text)
    doc.close()
    text = "\n\n".join(parts).strip()
    out_path.write_text(text, encoding="utf-8")
    return len(text)


def main():
    parser = argparse.ArgumentParser(description="对 PDF 做 OCR，输出到 <主题>-ocr.txt")
    parser.add_argument("pdf", type=Path, help="PDF 文件路径")
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=None,
        help="可选：输出 txt 路径；默认与 PDF 同目录，文件名为 <pdf 主名>-ocr.txt",
    )
    parser.add_argument("--dpi", type=int, default=200, help="渲染 DPI，默认 200")
    args = parser.parse_args()
    pdf_path = args.pdf.resolve()
    if not pdf_path.is_file():
        print(f"错误：文件不存在 {pdf_path}", file=sys.stderr)
        sys.exit(1)
    out_path = args.output if args.output is not None else pdf_path.parent / f"{pdf_path.stem}-ocr.txt"
    out_path = out_path.resolve()
    try:
        n = ocr_pdf(pdf_path, out_path, dpi=args.dpi)
    except Exception as e:
        print(f"错误：{e}", file=sys.stderr)
        sys.exit(1)
    if n == 0:
        print("警告：OCR 结果为空。", file=sys.stderr)
    print(out_path)


if __name__ == "__main__":
    main()
