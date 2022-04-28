# 基于Hurricane Electrics的免费DDNS脚本

## 基本实现
这只是一个简单的动态更新HE上的dns记录的python脚本，目前功能只能一次性的查询已有的一个域名空间内的所有记录，并通过[https://www.ipify.org](https://www.ipify.org)查询本机公网IP地址，再通过和HE上的记录进行比对，如果不同，则更新，否则不进行任何操作。

## 关于HE免费DNS

- HE free DNS站点：[https://dns.he.net/](https://dns.he.net/)
- 官方文档：[https://dns.he.net/docs.html](https://dns.he.net/docs.html)

## 使用前

1. 使用前,前往[HE free DNS](https://dns.he.net/)站点注册并登录,然后添加一个顶级域名，并在域名注册商网站将域名的DNS服务器改为：

   ```
   ns1.he.net
   ns2.he.net
   ns3.he.net
   ns4.he.net
   ns5.he.net
   ```
2. 点击`New A`，在`name`框中输入一个二级域名，选择合适的TTL，并勾选`Enable entry for dynamic dns`，点击`submit`
3. 点击二级域名后的`DDNS`栏中的刷新按钮，点击`generate key`，复制该key并保存，用于配置下文`config`中的`key`，然后点击`submit`

## 用法指南
1. 安装依赖：
   ```bash
   pip install dnspython requests
   ```
2. 下载本目录下的python脚本并上传至服务器，修改配置文件。由于脚本没有进行循环，请自行在服务器上利用crontab等工具，根据自己的情况，设置刷新频率。

## 配置
ddns信息的配置在`ddns_for_HE.py`的`conf`变量中：
- `dynUrl`: 字符串。默认为 `https://dyn.dns.he.net/nic/update?hostname=`，无需更改
- `TLD`: 字符串。顶级域名，如 `example.com`
- `names`: 列表：
    - `name`：字符串。子域名名称，如填写 `sub` ，完整链接则为：`sub.example.com`
    - `key`：字符串。[HE free DNS](https://dns.he.net/)的DDNS栏中的`key`