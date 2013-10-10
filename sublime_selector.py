import sublime_plugin

import replace
import webtask


class SelectorCommand(sublime_plugin.TextCommand):
    def run(self, edit, command=replace.ALPHA_NUM, **kwargs):
        for selection in self.view.sel():
            if selection.empty():
                continue

            text = self.view.substr(selection)
            replacement = self._process_string(text, command, **kwargs)
            self.view.replace(edit, selection, replacement)

    def _process_string(self, text, command, **kwargs):
        """Process the selected text using the appropriate function."""
        if command == replace.ALPHA_NUM:
            output_text = replace.alpha_num(text)
        elif command == replace.TITLIFY:
            output_text = replace.title(text)
        elif command == replace.SLUGIFY:
            output_text = replace.slugify(text)
        elif command == replace.CLASSIFY:
            output_text = replace.classify(text)
        elif command == replace.WRAP:
            output_text = replace.wrap(text, **kwargs)
        elif command == replace.URL_ENCODE:
            output_text = replace.url_encode(text)
        elif command == replace.URL_DECODE:
            output_text = replace.url_decode(text)
        elif command == webtask.GOOGLE:
            output_text = webtask.google_search(text)
        elif command == webtask.STACK:
            output_text = webtask.stackoverflow_search(text)

        return output_text
