# py3_http_utils

#### 介绍

Python3 Http Utils

#### 安装

```shell
  pip install py3_http_utils
```

### Response 使用说明

#### requests Response 使用说明

```python
# requests Response 使用说明
import requests
from requests import Response
from py3_http_utils.response import RequestsResponseHandler


def pretreatment(response: Response = None):
    """
    预处理response实例方法
    """
    response.encoding = response.apparent_encoding
    return response


# 执行请求
response = requests.get(url="https://www.baidu.com")

response = RequestsResponseHandler.handler(response=response, pretreatment=None, condition=lambda x: x.ok)

text = RequestsResponseHandler.text(response=response, pretreatment=pretreatment, condition=lambda x: x.ok)

content = RequestsResponseHandler.content(response=response, pretreatment=pretreatment, condition=lambda x: x.ok)

json = RequestsResponseHandler.json(response=response, pretreatment=pretreatment, condition=lambda x: x.ok)

json_addict = RequestsResponseHandler.json_addict(response=response, pretreatment=pretreatment,
                                                  condition=lambda x: x.ok)

beautifulsoup = RequestsResponseHandler.beautifulsoup(response=response, pretreatment=pretreatment,
                                                      condition=lambda x: x.ok)
```
#### httpx Response 使用说明

```python
# httpx Response 使用说明
import httpx
from httpx import Response
from py3_http_utils.response import HttpxResponseHandler


def pretreatment(response: Response = None):
    """
    预处理response实例方法
    """
    response.encoding = response.apparent_encoding
    return response


# 执行请求
response = httpx.get(url="https://www.baidu.com")

response = HttpxResponseHandler.handler(response=response, pretreatment=None, condition=lambda x: x.is_success)

text = HttpxResponseHandler.text(response=response, pretreatment=pretreatment, condition=lambda x: x.is_success)

content = HttpxResponseHandler.content(response=response, pretreatment=pretreatment, condition=lambda x: x.is_success)

json = HttpxResponseHandler.json(response=response, pretreatment=pretreatment, condition=lambda x: x.is_success)

json_addict = HttpxResponseHandler.json_addict(response=response, pretreatment=pretreatment,
                                               condition=lambda x: x.is_success)

beautifulsoup = HttpxResponseHandler.beautifulsoup(response=response, pretreatment=pretreatment,
                                                   condition=lambda x: x.is_success)
```