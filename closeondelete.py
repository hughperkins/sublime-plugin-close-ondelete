import sublime_plugin
import sublime
import os


class MyEvents(sublime_plugin.EventListener):
    def on_activated(self, view):
        if view.is_dirty():
            return
        filename = view.file_name()
        if not os.path.exists(filename):
            view.set_scratch(True)
            sublime.set_timeout(lambda: view.window().run_command("close_file"), 0)

