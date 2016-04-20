#coding=utf-8
from optparse import OptionParser
import subprocess
from datetime import date, time, datetime, timedelta

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

def cleanBuildDir():
	cleanCmd = "rm -rf ./build/"
	process = subprocess.Popen(cleanCmd, shell = True)
	process.wait()


def buildProject(project, target, output):
	#buildCmd = 'xcodebuild -project %s -target %s -sdk %s -configuration %s build CODE_SIGN_IDENTITY="%s" PROVISIONING_PROFILE="%s"' %(project, target, SDK, CONFIGURATION, CODE_SIGN_IDENTITY, PROVISIONING_PROFILE)
	process = subprocess.Popen("pwd", stdout=subprocess.PIPE)
	(stdoutdata, stderrdata) = process.communicate()
	
	buildArchiveCmd = 'xcodebuild -project %s.project -scheme %s archive -archivePath ./build/%s.xcarchive' %(targetName, targetName, targetName)
	process = subprocess.Popen(buildArchiveCmd, shell = True)
	process.wait()

	buildIpaCmd = 'xcodebuild -exportArchive -exportFormat ipa -archivePath build/%s.xcarchive -exportPath build/%s.ipa' %(targetName, ipaName)

	process = subprocess.Popen(buildIpaCmd, shell=True)
	(stdoutdata, stderrdata) = process.communicate()

def buildWorkspace(workspace, scheme, output):
	cleanBuildDir()
	
	process = subprocess.Popen("pwd", stdout=subprocess.PIPE)
	(stdoutdata, stderrdata) = process.communicate()
	
	buildArchiveCmd = 'xcodebuild -workspace %s.xcworkspace -scheme %s archive -archivePath ./build/%s.xcarchive' %(targetName, targetName, targetName)
	process = subprocess.Popen(buildArchiveCmd, shell = True)
	process.wait()

	buildIpaCmd = 'xcodebuild -exportArchive -exportFormat ipa -archivePath build/%s.xcarchive -exportPath build/%s.ipa' %(targetName, ipaName)
	process = subprocess.Popen(buildIpaCmd, shell=True)
	(stdoutdata, stderrdata) = process.communicate()

	
	

def xcbuild(options):
	#print "options: %s, args: %s" % (options, args)
	project = options.project
	workspace = options.workspace
	target = options.target
	scheme = options.scheme
	output = options.output

	if project is None and workspace is None:
		pass
	elif project is not None:
		buildProject(project, target, output)
	elif workspace is not None:
		buildWorkspace(workspace, scheme, output)

def main():
	
	parser = OptionParser()
	parser.add_option("-w", "--workspace", help="Build the workspace name.xcworkspace.", metavar="name.xcworkspace")
	parser.add_option("-p", "--project", help="Build the project name.xcodeproj.", metavar="name.xcodeproj")
	parser.add_option("-s", "--scheme", help="Build the scheme specified by schemename. Required if building a workspace.", metavar="schemename")
	parser.add_option("-t", "--target", help="Build the target specified by targetname. Required if building a project.", metavar="targetname")
	parser.add_option("-o", "--output", help="specify output filename", metavar="output_filename")

	(options, args) = parser.parse_args()

	

	xcbuild(options)

if __name__ == '__main__':
	main()