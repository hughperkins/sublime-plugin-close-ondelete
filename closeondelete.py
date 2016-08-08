import sublime_plugin
import sublime
import os


class MyEvents(sublime_plugin.EventListener):
    def on_activated(self, view):
        if view.is_dirty():
            return
        if view.command_history(0)[0] == '':  # means we just opened new file
            return
        filename = view.file_name()
        if filename is not None and not os.path.exists(filename):
            view.set_scratch(True)
            sublime.set_timeout(lambda: view.window().run_command("close_file"), 0)
