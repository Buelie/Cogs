# Cogs简介
<img src="https://camo.githubusercontent.com/c79826d5c66969e9301ca01d6147c4d0dab063e55dacb94624589cfeb8cedeb5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31302532422d677265656e">

### 仅能够在Python3.10+上运行!!!

***它是由 [清云工作室语言开发组©](#) 所开发的一门基于Python的面向对象开放的解释性语言,同时我们提供了它的构建工具--Bue和Waf(Bue是基于pip的,意味着如果使用Bue就需要安装pip.Waf基于Git,意味着如果使用Waf就需要安装git工具).我们提供了两个解释器,一个基于Python开发,一个基于C开发,如果您是个人使用,我们推荐Python解释器,如果是团队,我们推荐使用C解释器.***

# 特征
* 官方双语言解释器
* 语法简洁
* 官方解释器支持`.py`, `.cog`, `.cgs`三种后缀名
* 开源开放
* 多语言详细的开发文档
* 两种不同的构建工具
* 支持多平台(对`Linux,windows10`提供特别支持

# 解释器
***我们提供两个解释器,一个基于C(我们称他为C编译器),一个基于Python(我们称他为Py编译器),如果您需要下载解释器,可以才下面下载或者从[所有版本](#)下载***
| 资源 | exe | msi | zip | ARM64 | x32(exe) | x32(msi) |
| - | - | - | - | - | - | - |
| C编译器 | [V0.0.1.exe](#) | [V0.0.1.msi](#) | [V0.0.1.zip](#) | [V0.0.1.exe](#) | [V0.0.1.exe](#) | [V0.0.1.msi](#) |
| Py编译器 | [V0.0.1.exe](#) | [V0.0.1.msi](#) | [V0.0.1.zip](#) | [V0.0.1.exe](#) | [V0.0.1.exe](#) | [V0.0.1.msi](#) |

# Bue与Waf
***Bue与Waf是我们提供的Cogs构建工具,如果您需要他们,请才下面下载.详细信息见 [构建工具文档](#).***

| 资源 | exe | msi | zip | ARM64 | x32(exe) | x32(msi) |
| - | - | - | - | - | - | - |
| Bue构建工具 | [V0.0.1.exe](#) | [V0.0.1.msi](#) | [V0.0.1.zip](#) | [V0.0.1.exe](#) | [V0.0.1.exe](#) | [V0.0.1.msi](#) |
| Waf构建工具 | [V0.0.1.exe](#) | [V0.0.1.msi](#) | [V0.0.1.zip](#) | [V0.0.1.exe](#) | [V0.0.1.exe](#) | [V0.0.1.msi](#) |

# 构建您的第一个项目
首先找到一个您喜欢的文件夹,创建项目文件夹,在新文件夹内新建`bue.xml`(当你安装的构建工具是Bue时,创建此文件)或者`waf.xml`(当你安装的构建工具是Waf时,创建此文件)文件.创建`main.cgs`(或者`.py`和`.cog`),接着,在构建文件(`bue.xml`和`waf.xml`)中写如下内容:
```xml
<ver>0.0.1</ver> #项目版本
<name>Test</name> #项目名称
<project> #项目结构
  <main>main.cgs</main> #项目主文件
  <cons>Bue</cons> #项目构建工具(Waf或者Bue)
</project>
<wter>yydshmcl</wter> #项目作者或者作者邮箱
<inte>python</inte> #项目解释器(c或者python)
```
然后,您创建了您的第一个项目!!!

**What the? You don't understand Chinese? Try [Switch Language](#)**

# 您想用其他方式安装?
**测试使用pip安装!**
```
pip install CogsL
```

# 用pip进行更新:
```
pip install --upgrade CogsL
```
