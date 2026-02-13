#!/usr/bin/env python3
"""从 PDF 仅提取文本，输出到 news/<主题>-extract.txt。不处理图片。"""
import argparse
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("请先安装 PyMuPDF: pip install pymupdf", file=sys.stderr)
    sys.exit(1)


def extract_text(pdf_path: Path, out_path: Path) -> int:
    doc = fitz.open(pdf_path)
    chunks = []
    for page in doc:
        chunks.append(page.get_text())
    doc.close()
    text = "\n".join(chunks).strip()
    out_path.write_text(text, encoding="utf-8")
    return len(text)


def main():
    parser = argparse.ArgumentParser(description="提取 PDF 文本到 <主题>-extract.txt")
    parser.add_argument("pdf", type=Path, help="PDF 文件路径，如 news/xxx.pdf")
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=None,
        help="可选：输出 txt 路径；默认与 PDF 同目录，文件名为 <pdf 主名>-extract.txt",
    )
    args = parser.parse_args()
    pdf_path = args.pdf.resolve()
    if not pdf_path.is_file():
        print(f"错误：文件不存在 {pdf_path}", file=sys.stderr)
        sys.exit(1)
    stem = pdf_path.stem
    out_path = args.output if args.output is not None else pdf_path.parent / f"{stem}-extract.txt"
    out_path = out_path.resolve()
    try:
        n = extract_text(pdf_path, out_path)
    except Exception as e:
        print(f"错误：{e}", file=sys.stderr)
        sys.exit(1)
    if n == 0:
        print("警告：提取文本为空，可能为扫描件 PDF，请考虑先 OCR。", file=sys.stderr)
    print(out_path)


if __name__ == "__main__":
    main()
