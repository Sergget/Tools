import barcode
from barcode.writer import ImageWriter

def render(position_code):
    writer_option = {
        "text_distance": 3,
        "font_size": 36,
        "module_height": 36,
        "module_width": 1
    }
    code = barcode.get('code128', position_code, writer=ImageWriter())
    code.save("dest\\"+position_code, writer_option)

#批量打印
with open("input.txt") as f:
    while True:
        position_code = f.readline().replace("\n", "")
        if position_code == "":
            break
        else:
            render(position_code)

# 测试打印
# position_code = "A101"
# render(position_code)