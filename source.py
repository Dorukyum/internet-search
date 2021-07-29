import vscode

ext = vscode.Extension(
    "internet-search",
    "Internet Search",
    "0.0.1",
    "Use your default browser to search anything quickly",
    "./icon.png",
    {"type": "git", "url": "https://github.com/Dorukyum/internet-search"},
    "Dorukyum",
)
ext.set_default_category("Search")


@ext.command("DuckDuckGo")
def duckduckgo():
    command("duckduckgo", "")


@ext.command("Google")
def google():
    command("google", "search")


@ext.command("Bing")
def bing():
    command("bing", "search")


def command(engine, path):
    editor = vscode.window.ActiveTextEditor()
    if editor != vscode.ext.undefined:
        selection = editor.document.get_text(editor.selection)
        if selection:
            query = selection
        else:
            query = vscode.window.show_input_box(
                vscode.ext.InputBoxOptions("What would you like to search for?")
            )
    else:
        query = vscode.window.show_input_box(
            vscode.ext.InputBoxOptions("What would you like to search for?")
        )
    if not query:
        return

    vscode.env.open_external(
        f"https://www.{engine}.com/{path}?q={query.replace(' ', '+')}"
    )


vscode.build(ext, publish=True)
