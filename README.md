# dedecms-url-redirection
For web applications using DEDECMS 5.71SP1 and earlier, URL redirects occur because the source code logic error of the CMS does not judge the input GET request
使用dedecms 5.71sp1及以下版本的web应用，因为cms的源码逻辑错误未对输入的GET请求进行判断从而发生url重定向

How to use POC
poc使用方法

Just change the domain name of the target.txt
更改target.txt的域名即可

Sometimes the reason for the failure may be that the access to the primary domain automatically adds /index.html
有时候失败的原因可能是访问主域名会自动添加/index.html
