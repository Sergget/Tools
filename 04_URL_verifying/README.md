# URL存活性验证

## 用途

本工具用于读取`input.txt`内的内容，每行为1个url，将每个可访问的url存入`export.txt`，并将异常写入`error.txt`

## 使用

本工具在python 3.10下编写

- 使用前安装`requests`模块：

    ```bash
    pip install requests
    ```
- 编辑`input.txt`，输入需要测试的url，每行一条
- 运行以下命令

    ```bash
    python url_verifying.py
    ```
    可访问的url输出在`export.txt`文件中，异常信息输出在`error.txt`中