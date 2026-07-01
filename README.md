# selenium
selenium Browser 

## 无头浏览器登录脚本
> 需要设置的变量
> 
> Settings-->Secrets and variables--->actions--->
- Secrets
  - PASSWORD  [**必填**：设置账号的密码]
- Variables
  - ACCOUNTS  [**必填**：账号清单，逗号`,`间隔]
  - HY2_URL   [可选：Hysteria2代理连接]
  - TG_API    [可选：tg自定义接口]

> 使用Variables方便后期查看相关信息；便于修改。

> `HY2_URL` :正常使用hysteria2节点链接
```
hyteria2://UUID@IP:PORT?sni=www.bing.com
```
