import sublime, sublime_plugin
import subprocess

def minifyJs(fileName):
	if not fileName.endswith('.js'):
		print('file is not a javascript file, minification skipped')
		return

	outputFileName = fileName + '.min'
	cmd = ['uglifyjs', '--compress', '--mangle', '--output', outputFileName, '--', fileName]

	uglifyProcess = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = uglifyProcess.communicate()

	return error.decode('utf-8')


class MinifyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		fileToMinify = self.view.file_name()

		if not fileToMinify :
			print('File is not saved, minification skipped')
			return

		error = minifyJs(fileToMinify)
		if error :
			sublime.error_message(error)
		else :
			print('Minification has been completed successfully')

#listener to current js file
class LessToCssSave(sublime_plugin.EventListener):
  def on_post_save(self, view):
    view.run_command("minify")
