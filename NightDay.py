import sublime, sublime_plugin, sys, time

class change_nightCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		app_settings = sublime.load_settings("NightDay.sublime-settings")
		s = sublime.load_settings("../User/Preferences.sublime-settings")
		s.set("color_scheme", app_settings.get("night"))
		sublime.save_settings("../User/Preferences.sublime-settings")


class change_dayCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		app_settings = sublime.load_settings("NightDay.sublime-settings")
		s = sublime.load_settings("../User/Preferences.sublime-settings")
		s.set("color_scheme", app_settings.get("day"))
		sublime.save_settings("../User/Preferences.sublime-settings")

class change_enabledCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		app_settings = sublime.load_settings("NightDay.sublime-settings")
		if app_settings.get("automatic", "yes") == "yes":
			app_settings.set("automatic", "no")
		else:
			app_settings.set("automatic", "yes")
			doTimeCheck()

		sublime.save_settings("NightDay.sublime-settings")


def doTimeCheck():
	hour = time.strftime("%H")
	app_settings = sublime.load_settings("NightDay.sublime-settings")
	s = sublime.load_settings("../User/Preferences.sublime-settings")
	if int(hour) >= 20:
		if s.get("color_scheme") != app_settings.get("night") and s.get("color_scheme") == app_settings.get("day") and app_settings.get("automatic") == "yes":
			sublime.run_command("change_night")
	elif int(hour) >= 06:
		if s.get("color_scheme") != app_settings.get("day") and s.get("color_scheme") == app_settings.get("night") and app_settings.get("automatic") == "yes":
			sublime.run_command("change_day")

	if app_settings.get("automatic") == "yes":
		sublime.set_timeout(doTimeCheck, 60*1000) # 60 seconds

app_settings = sublime.load_settings("NightDay.sublime-settings")
if app_settings.has("automatic"):
	if app_settings.get("automatic") == "yes":
		doTimeCheck()
else:
	app_settings.set("automatic", "yes")
	sublime.save_settings("NightDay.sublime-settings")

if not app_settings.has("night"):
	app_settings.set("night", "{insert path to theme here}")
	sublime.save_settings("NightDay.sublime-settings")

if not app_settings.has("day"):
	app_settings.set("day", "{insert path to theme here}")
	sublime.save_settings("NightDay.sublime-settings")