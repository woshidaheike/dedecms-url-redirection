# CVE-2024-57241(CNNVD-2024-34500830)
For web applications using DEDECMS 5.71SP1 and earlier, URL redirects occur because the source code logic error of the CMS does not judge the input GET request
使用dedecms 5.71sp1及以下版本的web应用，因为cms的源码逻辑错误未对输入的GET请求进行判断从而发生url重定向

How to use POC
poc使用方法

Just change the domain name of the target.txt
更改target.txt的域名即可

Sometimes it fails because the website has a verification mechanism that needs to add user-agent, referer, etc. to the script
有时失败是因为网站有验证机制需要在脚本中添加user-agent，referer等等

Update or upgrade patches for earlier versions of DEDECMS
对低版本的dedecms进行更新或升级补丁
https://www.dedecms.com/download#changelog（DedeCMS V5.7.65）
