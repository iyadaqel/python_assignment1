""" An example of the `Notebook` widget.

This example demonstrates the use of the `Notebook` widget. A `Notebook`
displays its children as a tabbed control, where one child is visible
at a time. The children of a `Notebook` must be instances of `Page` and
parent of a `Page` must be a `Notebook`. A `Page` can have at most one
child which must be an instance of `Container`. This `Container` is
expanded to fill the available space in the page. A `Notebook` is layed
out using constraints just like normal constraints enabled widgets.

Implementation Notes:

    Changing the tab style of the `Notebook` dynamically is not
    supported on Wx. Close buttons on tabs is not supported on
    Wx when using the 'preferences' tab style.

<< autodoc-me >>
"""
from enaml.widgets.api import (
    Window, Notebook, Page, Container, PushButton, Field, Html, CheckBox
)


enamldef main(Window):
    Container:
        Notebook: nbook:
            tab_style = 'preferences'
            Page:
                title = 'Foo Page'
                closable = False
                tool_tip = 'Foo Page here'
                Container:
                    PushButton:
                        text = 'Open Bar Page'
                        clicked :: bar.open()
                    PushButton:
                        text = 'Open Baz Page'
                        clicked :: baz.open()
                    CheckBox:
                        text = 'Tabs Closable'
                        checked := nbook.tabs_closable
                    CheckBox:
                        text = 'Tabs Movable'
                        checked := nbook.tabs_movable
                    CheckBox:
                        text = 'Document Style Tabs'
                        checked << nbook.tab_style == 'document'
                        toggled ::
                            if checked:
                                nbook.tab_style = 'document'
                            else:
                                nbook.tab_style = 'preferences'
            Page: bar:
                title = 'Bar Page'
                Container:
                    Field:
                        pass
                    Field:
                        pass
                    Field:
                        pass
            Page: baz:
                title = 'Baz Page'
                Container:
                    padding = 0
                    Html:
                        source = '<h1><center>Hello World!</center></h1>'
