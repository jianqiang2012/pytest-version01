## 项目结构

- api ===> api目录文件统一存放http接口访问地址,接口封装层，将HTTP接口分装为Python3的接口
- common ===> 存放工具
- base ===> requests 请求方法封装，基础方法
- data ===> 测试数据管理，文件，yaml，json等
- pytest.ini ===> pytest的配置文件，定义了哪些是测试用例
- requirements.txt ===> 依赖文件
- testcases ===> 测试用例层
- config ===> 配置文件
- operation ===> 关键字封装层
- testcases ===> 这里就是放我们用例的地方
- vo 层是预留来传参数的
- testcases/single_api/data_top_list_test.py ===> 单接口的测试用例层，这里提供了一个用例开发模版
- log 层存放日志使用

-- 如何启动框架？
直接使用 pytest -s -v 目录/文件