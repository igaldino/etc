#!/usr/bin/env python3

# https://bitbucket.org/confluence/fluxbox-tools

# To generate a menu:
# fbxdgmenu.py > ~/.fluxbox/applications-menu

# Menu entry for including a generated submenu:
# [include] (YOUR_HOME_DIR/.fluxbox/applications-menu)

# Menu entry for regenerating the menu:
# [exec] (Regenerate menu) {/PATH/TO/fbxdgmenu.py > YOUR_HOME_DIR/.fluxbox/applications-menu}

from __future__ import print_function
from xdg import Menu
import sys
import re

STANDALONE=False

TERMINAL_COMMAND = "konsole -e %s"
TERMINAL_PATH_COMMAND = "konsole --workdir %s -e %s"

REMOVE_FROM_EXEC = re.compile(' -caption "?%c"?| -[^ ]+ %[UuFf]| %[UuFfi]')

class FluxboxXDGMenu:
    def __init__(self, standalone=False, filename=None):
        menu = Menu.parse(filename)

        if standalone:
            self.contents = "[begin] (Fluxbox)"
            self.contents.extend(self.menu(menu, depth=1))
            self.comtents.append("[end]")
        else:
            self.contents = self.menu(menu)

    def __str__(self):
        return "\n".join(self.contents)

    def menu(self, menu, depth=0):
        contents = []

        indent = " " * 4 * depth
        name = menu.getName()
        contents.append("%s[submenu] (%s)" % (indent, name))

        for entry in menu.getEntries():
            if isinstance(entry, Menu.MenuEntry):
                try:
                    contents.append(self.entry(entry, depth + 1))
                except ValueError as e:
                    sys.stderr.write(str(e))
                    continue
            elif isinstance(entry, Menu.Menu):
                contents.extend(self.menu(entry, depth + 1))
            elif isinstance(entry, Menu.Separator):
                contents.append(self.separator(depth + 1))

        contents.append("%s[end]" % indent)

        return contents

    def entry(self, entry, depth):
        indent = " " * 4 * depth
        name = entry.DesktopEntry.getName()

        d_exec = entry.DesktopEntry.getExec()

        if not d_exec:
            raise ValueError("No executable information found for entry '%s' (%s)." % (name, entry))

        executable = REMOVE_FROM_EXEC.sub('', d_exec)
        path = entry.DesktopEntry.getPath()
        terminal = entry.DesktopEntry.getTerminal()

        if path and terminal:
            command = TERMINAL_PATH_COMMAND % (path, executable)
        elif terminal: # and not path
            command = TERMINAL_COMMAND % executable
        elif path: # and not terminal
            command = "cd %s; %s" % (path, executable)
        else: # if neither
            command = executable

        return "%s[exec] (%s) {%s}" % (indent, name, command)

    def separator(self, depth):
        indent = " " * 4 * depth
        return "%s[separator]" % indent

filename = sys.argv[1] if len(sys.argv) > 1 else None
print(FluxboxXDGMenu(standalone=STANDALONE, filename=filename))
