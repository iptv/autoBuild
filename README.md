# autoBuild
iOS自动打包iPa

使用方法:
1. 脚本文件拷贝至项目根目录
2. 在脚本文件编辑如下信息
################ 配置信息 #############
#工程名
targetName="JuXiangZhuan"

#版本
tag = "v1.0"

#Release Debug
buildConfiguration = "Release"

#时间戳
#timestamp = datetime.now().strftime('%Y_%m_%d %H:%M:%S')
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

#渠道号 默认AppStore
channelId = "AppStore"

#包名
ipaName = targetName + "_" + timestamp + "_" + tag + "_" + buildConfiguration + "_" + channelId

########## 配置结束 ##################

3.在终端, cd至项目根目录, 如果是工作区间, 执行 python autobuild.py -w yourname.xcworkspace 命令; 如果是单一工程, 执行  python autobuild.py -p yourname.project