import pprint

import requests

html_content = """
<!doctype html>
   <html lang="en">
      <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <meta name="description" content="Aliyun Vulnerability Database">
         <title>
            阿里云漏洞库
         </title>
            <!-- Bootstrap core CSS -->         <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon"/>
         <link href="/static/css/bootstrap.min.css" rel="stylesheet">
         <link href="/static/css/skybox.css" rel="stylesheet">
         <link rel="stylesheet" href="/static/bootstrap-icons-1.2.2/font/bootstrap-icons.css">
         <script src="/static/js/jquery.slim.min.js"></script><script src="/static/js/popper.min.js"></script><script src="/static/js/bootstrap.min.js"></script>
         <style>
            #main .container {            min-width: 1300px;        }        #main .attr-item:nth-child(2) {            margin-left: 3px;            margin-right: 3px;        }        .product-box > div {            word-break: break-all;        }        .bs-tooltip-right > .tooltip-inner {            min-width: 300px;        }        .popover{            max-width: 100%; /* Max Width of the popover (depending on the container!) */        }    
         </style>
</head>
      <body>
         <header class="navigation">
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
               <a class="navbar-brand pl-2 pl-md-4 pr-2" href="/" style="padding: 0;"><img src="/static/img/aliyun-my_code.png" height="30px" style="margin-bottom: 4px;"><span style="font-size: 24px; font-weight: 500; padding-left: 5px;">                                            阿里云漏洞库                                    </span></a><button class="navbar-toggler" type="button" data-target="#navbarsExampleDefault" data-toggle="collapse"><span class="navbar-toggler-icon"></span></button>
               <div class="navbar-collapse collapse" id="navbarsExampleDefault">
                  <ul class="navbar-nav mr-auto">
                     <li class="nav-item">
                        <a class="nav-link active" href="/high-risk/list">高危漏洞</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link " href="/nvd/list">CVE 漏洞库</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link " href="/nonvd/list">非CVE漏洞库</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link " href="https://xz.aliyun.com/" target="_blank">安全社区</a>
                     </li>
</ul>
                  <form class="form-inline my-2 my-lg-0" action="/search" method="get">
                     <input class="form-control mr-sm-2" type="search" name="q" value=""                       placeholder="搜索漏洞"                       aria-label="Search" autocomplete="off" style="width: 240px;"><button class="btn btn-outline-light my-2 my-sm-0" type="submit">搜索</button>
                  </form>
</div>
</nav>
</header>
         <style>
            a {        color: #4b45a1;    }    a:hover {        color: #4b45a1;        text-decoration: underline;    }    .header__content {        margin-left: auto;        margin-right: auto;        max-width: 90rem    }    .header__title {        font-variant: common-ligatures proportional-nums;        font-weight: 500;        line-height: 1;        text-rendering: optimizeLegibility;        margin-bottom: .5rem    }    .header__title {        font-size: 36px    }    .header__lede {        font-variant: common-ligatures proportional-nums;        font-weight: 400;        line-height: 1.25;        text-rendering: optimizeLegibility;        margin-bottom: 0    }    .header__lede {        font-size: 20px    }    .table th {        border-top: 0px solid #dee2e6;    }    .btn-bd-primary {        font-weight: 400;        color: #0056b3;        border-radius: 15px;    }    .nav-pills .nav-link.active, .nav-pills .show > .nav-link {        color: #fff;        background-color: #4b4f54;    }
         </style>
         <main role="main">
            <div class="album py-4" id="itl-header">
               <div class="container vuln-list-container">
                  <div class="header__content">
                     <div class="header__text">
                        <h1 class="header__title ">
                           高危漏洞库
                        </h1>
                        <div class="header__lede">
                           阿里云安全专家专业评估分析，帮助客户精准研判高危风险漏洞。
                        </div>
</div>
</div>
</div>
</div>
            <div class="py-3 bg-light">
               <div class="container vuln-list-container">
                  <div class="py-3">
                     <div class="d-flex justify-content-between align-items-center">
                        <a class="px-3 btn btn-sm btn-outline-secondary btn-bd-primary disabled" href="?page=0"> « 上一页 </a><span class="text-muted" style="text-overflow: ellipsis;white-space: nowrap;  overflow: hidden;">第 1 页 / 49 页  •  总计 1463 条记录</span><a class="px-3 btn btn-sm btn-outline-secondary btn-bd-primary " href="?page=2"> 下一页 » </a>
                     </div>
</div>
            <div class="my-3 px-3 pt-2 bg-white rounded shadow-sm table-responsive">
               <table class="table">
                  <thead>
                     <tr>
                        <th scope="col" style="width: 180px;" nowrap="nowrap">
                           AVD编号
                        </th>
                        <th scope="col" style="width: 60%;" nowrap="nowrap">
                           漏洞名称
                        </th>
                        <th scope="col" nowrap="nowrap">
                           漏洞类型
                        </th>
                        <th scope="col" style="width: 120px;" nowrap="nowrap">
                           披露时间
                        </th>
                        <th scope="col" nowrap="nowrap">
                           漏洞状态
                        </th>
</tr>
</thead>
                  <tbody>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-49785" target="_blank">                                AVD-2023-49785                            </a>
                        </td>
                        <td>
                           NextChat cors SSRF 漏洞（CVE-2023-49785）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="服务端请求伪造（SSRF）">                                CWE-918                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-03-12                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-49785">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-warning btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="EXP 已公开">EXP                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-27198" target="_blank">                                AVD-2024-27198                            </a>
                        </td>
                        <td>
                           Teamcity 认证绕过致代码执行漏洞（CVE-2024-27198）	
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="使用候选路径或通道进行的认证绕过">                                CWE-288                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-03-05                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2024-27198">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-primary btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="POC 已公开">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-27199" target="_blank">                                AVD-2024-27199                            </a>
                        </td>
                        <td>
                           TeamCity 权限绕过漏洞（CVE-2024-27199）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="对路径名的限制不恰当（路径遍历）">                                CWE-22                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-03-05                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2024-27199">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-primary btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="POC 已公开">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-50380" target="_blank">                                AVD-2023-50380                            </a>
                        </td>
                        <td>
                           Apache Ambari &lt; 2.7.8 XXE（CVE-2023-50380）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="XML外部实体引用的不恰当限制（XXE）">                                CWE-611                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-02-28                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-50380">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="暂无可利用代码">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-50379" target="_blank">                                AVD-2023-50379                            </a>
                        </td>
                        <td>
                           Apache Ambari 命令注入漏洞（CVE-2023-50379）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="对生成代码的控制不恰当（代码注入）">                                CWE-94                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-02-27                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-50379">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="暂无可利用代码">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-25600" target="_blank">                                AVD-2024-25600                            </a>
                        </td>
                        <td>
                           Wordpress Bricks Builder 主题插件代码执行漏洞（CVE-2024-25600）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm">                                未定义                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-02-21                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2024-25600">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-primary btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="POC 已公开">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-22024" target="_blank">                                AVD-2024-22024                            </a>
                        </td>
                        <td>
                           Ivanti Pulse Connect Secure VPN XXE 漏洞（CVE-2024-22024）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="XML外部实体引用的不恰当限制（XXE）">                                CWE-611                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-02-13                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2024-22024">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-warning btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="EXP 已公开">EXP                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-50292" target="_blank">                                AVD-2023-50292                            </a>
                        </td>
                        <td>
                           Apache Solr Schema Designer 代码执行漏洞 (CVE-2023-50292)
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="关键资源的不正确权限授予">                                CWE-732                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-02-10                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-50292">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-primary btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="POC 已公开">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-50386" target="_blank">                                AVD-2023-50386                            </a>
                        </td>
                        <td>
                           Apache Solr Backup/Restore APIs 代码执行漏洞（CVE-2023-50386）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="危险类型文件的不加限制上传">                                CWE-434                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-02-10                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-50386">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-primary btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="POC 已公开">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-23917" target="_blank">                                AVD-2024-23917                            </a>
                        </td>
                        <td>
                           TeamCity 权限绕过漏洞（CVE-2024-23917）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="关键功能的认证机制缺失">                                CWE-306                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-02-06                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2024-23917">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="暂无可利用代码">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-25065" target="_blank">                                AVD-2024-25065                            </a>
                        </td>
                        <td>
                           Apache OFBiz 路径遍历致权限绕过漏洞（CVE-2024-25065）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm">                                未定义                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-02-04                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2024-25065">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="暂无可利用代码">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-21626" target="_blank">                                AVD-2024-21626                            </a>
                        </td>
                        <td>
                           runc 文件描述符泄漏漏洞（CVE-2024-21626）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="将文件描述符暴露给不受控制的范围（文件描述符泄露）">                                CWE-403                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-02-02                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2024-21626">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-primary btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="POC 已公开">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-24747" target="_blank">                                AVD-2024-24747                            </a>
                        </td>
                        <td>
                           MinIO 权限提升漏洞（CVE-2024-24747）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="特权管理不恰当">                                CWE-269                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-02-01                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2024-24747">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="暂无可利用代码">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-21893" target="_blank">                                AVD-2024-21893                            </a>
                        </td>
                        <td>
                           Ivanti Pulse Connect Secure VPN SSRF致远程代码执行漏洞（CVE-2024-21893）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="服务端请求伪造（SSRF）">                                CWE-918                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-02-01                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2024-21893">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-danger btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="漏洞利用攻击武器化">武器化                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-44313" target="_blank">                                AVD-2023-44313                            </a>
                        </td>
                        <td>
                           Apache ServiceComb Service-Center SSRF漏洞(CVE-2023-44313)
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="服务端请求伪造（SSRF）">                                CWE-918                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-01-31                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-44313">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="暂无可利用代码">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-0402" target="_blank">                                AVD-2024-0402                            </a>
                        </td>
                        <td>
                           GitLab workspace 任意文件写入漏洞（CVE-2024-0402）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="对路径名的限制不恰当（路径遍历）">                                CWE-22                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-01-26                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2024-0402">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="暂无可利用代码">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-23897" target="_blank">                                AVD-2024-23897                            </a>
                        </td>
                        <td>
                           Jenkins CLI 任意文件读取漏洞（CVE-2024-23897）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm">                                未定义                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-01-25                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2024-23897">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="暂无可利用代码">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-23946" target="_blank">                                AVD-2024-23946                            </a>
                        </td>
                        <td>
                           Apache OFBiz 目录遍历与文件包含漏洞 (CVE-2024-23946)
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="对路径名的限制不恰当（路径遍历）">                                CWE-22                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-01-24                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2024-23946">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="暂无可利用代码">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-1706412" target="_blank">                                AVD-2024-1706412                            </a>
                        </td>
                        <td>
                           亿赛通电子文档安全管理系统 文件上传漏洞
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm">                                未定义                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-01-23                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="无CVE">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="暂无可利用代码">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-0204" target="_blank">                                AVD-2024-0204                            </a>
                        </td>
                        <td>
                           Goanywhere MFT 未授权创建管理员漏洞（CVE-2024-0204）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="直接请求（强制性浏览）">                                CWE-425                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-01-23                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2024-0204">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-warning btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="EXP 已公开">EXP                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2024-22233" target="_blank">                                AVD-2024-22233                            </a>
                        </td>
                        <td>
                           Spring Framework 拒绝服务漏洞 (CVE-2024-22233)
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm">                                未定义                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-01-22                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2024-22233">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="暂无可利用代码">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-22527" target="_blank">                                AVD-2023-22527                            </a>
                        </td>
                        <td>
                           Atlassian Confluence 模板注入代码执行漏洞（CVE-2023-22527）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="Improper Neutralization of Special Elements Used in a Template Engine">                                CWE-1336                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-01-16                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-22527">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="暂无可利用代码">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-46226" target="_blank">                                AVD-2023-46226                            </a>
                        </td>
                        <td>
                           Apache IotDB UDF代码执行漏洞（CVE-2023-46226）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm">                                未定义                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-01-15                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-46226">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="暂无可利用代码">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-46805" target="_blank">                                AVD-2023-46805                            </a>
                        </td>
                        <td>
                           Ivanti Pulse Connect Secure VPN 远程代码执行（CVE-2023-46805）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="认证机制不恰当">                                CWE-287                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-01-13                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-46805">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-danger btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="漏洞利用攻击武器化">武器化                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-50290" target="_blank">                                AVD-2023-50290                            </a>
                        </td>
                        <td>
                           Apache Solr 环境变量信息泄漏漏洞（CVE-2023-50290）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="信息暴露">                                CWE-200                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-01-13                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-50290">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-primary btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="POC 已公开">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-7028" target="_blank">                                AVD-2023-7028                            </a>
                        </td>
                        <td>
                           GitLab 任意用户密码重置漏洞（CVE-2023-7028）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="忘记口令恢复机制弱">                                CWE-640                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-01-11                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-7028">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-danger btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="漏洞利用攻击武器化">武器化                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-49442" target="_blank">                                AVD-2023-49442                            </a>
                        </td>
                        <td>
                           Jeecg jeecgFormDemoController JNDI代码执行漏洞（CVE-2023-49442）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="可信数据的反序列化">                                CWE-502                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2024-01-04                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-49442">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-primary btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="POC 已公开">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-51467" target="_blank">                                AVD-2023-51467                            </a>
                        </td>
                        <td>
                           Apache OFBiz groovy 远程代码执行漏洞（CVE-2023-51467）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="服务端请求伪造（SSRF）">                                CWE-918                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2023-12-26                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-51467">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-primary btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="POC 已公开">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-50968" target="_blank">                                AVD-2023-50968                            </a>
                        </td>
                        <td>
                           Apache OFBiz 任意文件属性读取与SSRF漏洞（CVE-2023-50968）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="信息暴露">                                CWE-200                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2023-12-26                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-50968">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-primary btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="POC 已公开">PoC                            </button>
                        </td>
</tr>
                     <tr>
                        <td nowrap="nowrap">
                           <a href="/detail?id=AVD-2023-32725" target="_blank">                                AVD-2023-32725                            </a>
                        </td>
                        <td>
                           Zabbix Server session 泄漏漏洞（CVE-2023-32725）
                        </td>
                        <td nowrap="nowrap">
                           <button type="button" nowrap="nowrap" class="btn btn-outline-secondary btn-sm"                                    data-container="body"                                    data-toggle="tooltip" data-placement="top"                                    title="在信任Cookie未进行验证与完整性检查">                                CWE-565                            </button>
                        </td>
                        <td nowrap="nowrap">
                           2023-12-18                                                    
                        </td>
                        <td nowrap="nowrap">
                           <!--                            -->
                           <button type="button" class="btn  btn-outline-info btn-sm" data-toggle="tooltip"                                        data-placement="top"                                        title="CVE-2023-32725">CVE                                </button>
                           <!--                            -->
                           <button type="button" class="btn  btn-light btn-sm" data-toggle="tooltip"                                    data-placement="top"                                    title="暂无可利用代码">PoC                            </button>
                        </td>
</tr>
</tbody>
</table>
</div>
            <div class="d-flex py-3 justify-content-between align-items-center">
               <a class="px-3 btn btn-sm btn-outline-secondary btn-bd-primary disabled" href="?page=0"> « 上一页 </a><span class="text-muted" style="text-overflow: ellipsis;white-space: nowrap;  overflow: hidden;">第 1 页 / 49 页  •  总计 1463 条记录</span><a class="px-3 btn btn-sm btn-outline-secondary btn-bd-primary " href="?page=2"> 下一页 » </a>
            </div>
</div>
</div>
</main>
         <footer class="text-muted bg-dark">
            <div class="px-sm-5 px-3">
               <p class="float-right">
                  <a class="btn" href="#">回到顶部</a>
               </p>
               <p id="footer" style="padding-bottom:10px; border-bottom: 1px solid #595959;">
                  <a class="btn pl-0" href="/about">联系我们</a><a class="btn" href="/policy">                披露原则            </a>
               </p>
               <p class="pt-2">
                  <!-- -->
                  2024
                  <!-- -->
                   Alibaba Cloud Security Team. All Rights Reserved. NVDB备-20230014号.
               </p>
</div>
</footer>
         <script>    $(function () {        $('[data-toggle="tooltip"]').tooltip()    });</script>
      </body>
</html>
"""

from bs4 import BeautifulSoup

def analyze_vuln_page():
    soup = BeautifulSoup(html_content, 'html.parser')
    ret = []
    div_tag = soup.find(class_='my-3 px-3 pt-2 bg-white rounded shadow-sm table-responsive')
    if not div_tag:
        return ret
    if not (table := div_tag.table):
        return ret
    if not (tbody := table.tbody):
        return ret
    for tr_tag in tbody.find_all('tr'):
        item_dict = {}
        if not (a_tag := tr_tag.find('a')):
            continue
        avd_code = a_tag.get_text(strip=True)
        item_dict['avd_code'] = avd_code
        if not (status_tag := tr_tag.find_all('td')[4]):
            continue
        tags_list = []
        for button_tag in status_tag.find_all('button'):
            title_val = button_tag.get('title')
            match title_val:
                case '无CVE':
                    continue
                case 'POC 已公开':
                    item_dict['isPOC'] = '是'
                    continue
                case 'EXP 已公开':
                    item_dict['isEXP'] = '是'
                    continue
                case _:
                    # 暂无可利用代码、cve编号、
                    tags_list.append(title_val)
        if tags_list:
            item_dict['tags'] = tags_list
        ret.append(item_dict)
    pprint.pprint(ret)





def analyze_detail_page(file_name):
    with open(file_name, 'r') as f:
        detail_content = f.read()
    # soup = BeautifulSoup(detail_content, 'html.parser')
    soup = ALYAnalyzeBeautifulSoup(detail_content, 'html.parser')
    vuln_info = {}
    vuln_info.update(soup.extract_title_and_level())
    vuln_info.update(soup.extract_metric())
    vuln_info.update(soup.extract_describe_suggest())
    vuln_info.update(soup.extract_cwe_id_vuln_type())
    vuln_info.update(soup.extract_manufacture())
    pprint.pprint(vuln_info)


def remove_empty_lines(text):
    lines = text.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    result = '\n'.join(non_empty_lines)
    return result


class ALYAnalyzeBeautifulSoup(BeautifulSoup):

    def extract_title_and_level(self):
        ret = {}
        level_tag = self.find(class_='header__title')
        level = level_tag.find(attrs={'class': 'badge'})
        if level:
            ret['level'] = level.get_text(strip=True)
        title = level_tag.find(attrs={'class': 'header__title__text'})
        if title:
            ret['title'] = title.get_text(strip=True)
        return ret

    def extract_metric(self):
        metric_tags = self.find_all(attrs={'class': 'metric'})
        ret = {}
        for item_tag in metric_tags:
            label = item_tag.find(attrs={'class': 'metric-label'})
            value = item_tag.find(attrs={'class': 'metric-value'})
            label = label.string.strip()
            value = value.string.strip()
            match label:
                case 'CVE编号':
                    ret['cve_id'] = value
                case '利用情况':
                    ret['utilization'] = value
                case '补丁情况':
                    ret['patch'] = value
                case '披露时间':
                    ret['public_time'] = value
        return ret

    def extract_describe_suggest(self):
        main_tags = self.find(attrs={'class': 'py-4 pl-4 pr-4 px-2 bg-white rounded shadow-sm'})
        ret = {}

        for item_tag in main_tags.find_all(attrs={'class': 'border-bottom border-gray pb-2 mb-0'}):
            if not item_tag:
                continue
            label = item_tag.get_text(strip=True)
            # value = value.string.strip()
            match label:
                case '漏洞描述':
                    describe_tag = main_tags.find(attrs={'class': 'text-detail pt-2 pb-4'})
                    if not describe_tag:
                        continue
                    describe = ''
                    for div_tag in describe_tag.contents:
                        if des_info := div_tag.get_text(strip=True):
                            des_info = des_info.replace(' ', '')
                            describe += f'{des_info}\n'
                    ret['describe'] = describe
                case '解决建议':
                    describe_tag = main_tags.find_all(attrs={'class': 'text-detail pt-2 pb-4'})
                    if not describe_tag:
                        continue
                    if len(describe_tag) < 2:
                        continue
                    ret['referenceInformation'] = describe_tag[1].get_text(strip=True)

        reference_information_tag = main_tags.find(attrs={'class': 'text-detail pb-3 pt-2 reference'})
        if reference_information_tag:
            if not (table_tag := reference_information_tag.table):
                return ret
            reference_information_list = []
            for link in table_tag.find_all('a'):
                if not (href := link.get('href', '')):
                    continue
                reference_information_list.append(href)
            ret['repairSuggestion'] = reference_information_list
        return ret

    def extract_cwe_id_vuln_type(self):
        ret = {}
        type_div_tag = self.find_all('div', class_='table-responsive')
        if len(type_div_tag) < 2:
            type_div_tag = type_div_tag[0]
        else:
            type_div_tag = type_div_tag[1]
        table_tag = type_div_tag.table
        if not table_tag:
            return ret
        cwe_id_list = []
        vuln_type_list = []
        for tr in table_tag.find_all('tr'):
            tds = tr.find_all('td')
            cwe_id = tds[0].get_text(strip=True)
            vuln_type = tds[1].get_text(strip=True)
            if cwe_id == 'CWE-ID':
                continue
            cwe_id_list.append(cwe_id)
            vuln_type_list.append(vuln_type)
        ret['cwe_id'] = cwe_id_list
        ret['vuln_type'] = vuln_type_list
        return ret

    def extract_manufacture(self):
        ret = {}
        type_div_tag = self.find('div', class_='pb-4 pt-3 table-responsive')
        if not type_div_tag:
            return ret
        table_tag = type_div_tag.table
        if not table_tag:
            return ret
        manufacture_list = []
        product_list = []
        cpe_list = []
        for tr in table_tag.find_all('tr'):
            tds = tr.find_all('td', class_='bg-light')
            if not tds:
                continue
            manufacture = tds[1].get_text(strip=True)
            if manufacture == '厂商':
                continue
            manufacture_list.append(manufacture)
            product = tds[2].get_text(strip=True)
            product_list.append(product)
            _type = tds[0].get_text(strip=True)
            if _type == '应用':
                cpe_type = '/a'
            elif _type == '系统':
                cpe_type = '/o'
            elif _type == '硬件':
                cpe_type = '/h'
            else:
                cpe_type = '/*'
            _version = tds[3].get_text(strip=True)
            cpe_str = ':'.join(['cpe', cpe_type, manufacture, product, _version])
            cpe_list.append(cpe_str)
        ret['affectProduct'] = list(set(product_list))
        ret['affectVendor'] = list(set(manufacture_list))
        ret['vulnCPE'] = list(set(cpe_list))
        return ret


def test_request():
    url = 'https://avd.aliyun.com/high-risk/list?page=1'
    url= 'https://console-mock.apipost.cn/mock/71311695-8df1-49e2-96e5-786eddaa0c3d/high-risk/list?page=1&apipost_id=946378'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/sign",
        "Host": "avd.aliyun.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    rep = requests.get(url=url, headers={})
    print(rep.status_code)
    print(type(rep.status_code))
    print(type(rep.text))
    print(rep.text)
    print(rep.content)


if __name__ == '__main__':
    analyze_detail_page('vendor_detail_page.html')
    # analyze_vuln_page()
    # test_request()

