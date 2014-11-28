import sublime, sublime_plugin, sys, time

app_settings = sublime.load_settings("NightDay.sublime-settings")

class change_nightCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		s = sublime.load_settings("../User/Preferences.sublime-settings")
		s.set("color_scheme", app_settings.get("night"))
		sublime.save_settings("../User/Preferences.sublime-settings")


class change_dayCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		s = sublime.load_settings("../User/Preferences.sublime-settings")
		s.set("color_scheme", app_settings.get("day"))
		sublime.save_settings("../User/Preferences.sublime-settings")

'''
def doTimeCheck():
	hour = time.strftime("%H")
	s = sublime.load_settings("../User/Preferences.sublime-settings")
	if int(hour) >= 20:
		if s.get("color_scheme") != app_settings.get("night"):
			if s.get("color_scheme") == app_settings.get("day"):
				sublime.run_command("change_night")
	elif int(hour) >= 06:
		if s.get("color_scheme") != app_settings.get("day"):
			if s.get("color_scheme") == app_settings.get("night"):
				sublime.run_command("change_day")

sublime.set_timeout(doTimeCheck, 600000) # 10 minutes
'''