# 条形码生成器

## 用途

本工具用于读取`input.txt`内的内容，将每行内容分别生成一个条形码，条形码采用code128标准

## 使用

本工具在python 3.10下编写

- 使用前安装`pillow`、`python-barcode`模块：

    ```bash
    pip install pillow python-barcode
    ```
- 编辑`input.txt`，输入需要制作的条形码内容，每行一条
- 运行以下命令

    ```bash
    python barcode_generate.py
    ```
    生成的条形码在`dest`目录中

## 配置

生成的条形码的格式可修改，在`barcode_generate.py`修改如下配置：

```python
    writer_option = {
        "text_distance": 3, # 文字到条码的距离
        "font_size": 36, # 文字字体大小
        "module_height": 36, # 模块条码的高度，单位mm
        "module_width": 1 # 单一模块条码的宽度，单位mm
    }
```
具体其他配置可参考：[barcode文档](https://python-barcode.readthedocs.io/en/stable/writers/index.html)

