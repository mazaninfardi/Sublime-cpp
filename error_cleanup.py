import sublime, sublime_plugin
import re

class ErrorCleanupCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    region = sublime.Region(0, self.view.size())
    content = self.view.substr(region)
    self.view.replace(edit, region, re.sub(r"std::", r"", content))
