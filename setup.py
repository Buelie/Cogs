
from setuptools import setup find_packages
setup(name='CogsL',
      version='0.0.1',
      description='An interpretive language',
      author='GitHub-Buelie',
      author_email='yydshmcl@outlook.com',
      requires= ['random','matplotlib','os'], # 定义依赖哪些模块
      packages=find_packages(),  # 系统自动从当前目录开始找包
      # 如果有的包不用打包，则只能指定需要打包的文件
      #packages=['代码1','代码2','__init__']
      license="MIT License"
      )
