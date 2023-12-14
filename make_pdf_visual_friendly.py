import sys
import fitz  # PyMuPDF
import argparse
import os

def convert(input_pdf_name, output_pdf_name):
    background_color = (185/255, 231/255, 186/255)
    doc = fitz.open(input_pdf_name)
    print('Start converting......')
    for page in doc:
        page.draw_rect(page.rect, color=None, fill=background_color, overlay=False)

    doc.ez_save(output_pdf_name)
    doc.close()
    print("Background color changed and saved to:", output_pdf_name)

def main():
    # 1. 定义命令行解析器对象
    parser = argparse.ArgumentParser(description='Make your pdf visual friendly, useful for paper reading~')
    # 2. 添加命令行参数
    parser.add_argument('-i', type=str, required=True, help='path to the input pdf file', metavar='input_pdf_path', dest='input_pdf_name')
    parser.add_argument('-o', type=str, required=True, help='path to save the converted pdf file', metavar='output_pdf_path', dest='output_pdf_name')
    # 3. 从命令行中结构化解析参数
    args = parser.parse_args()
    input_pdf_name = args.input_pdf_name
    output_pdf_name = args.output_pdf_name

    print(f'PDF file to convert: {input_pdf_name}')
    print(f'Output path: {output_pdf_name}')
    if not os.path.exists(input_pdf_name):
        print(f'Error! File {input_pdf_name} cannot found!')
    convert(input_pdf_name, output_pdf_name)
    print('Thanks for using.')
    print('Bye Bye~')

if __name__ == '__main__':
    main()