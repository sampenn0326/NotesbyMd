import re

FORMULA = re.compile(r"^ {0,3}\$\$[ \t]*(.+?)[ \t]*\$\$[ \t]*$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")


def on_page_markdown(markdown, **kwargs):
    result = []
    fence_char = None
    fence_length = 0

    for line in markdown.splitlines(keepends=True):
        marker = FENCE.match(line)

        if fence_char is not None:
            result.append(line)
            if (
                marker
                and marker[1][0] == fence_char
                and len(marker[1]) >= fence_length
                and not marker[2].strip()
            ):
                fence_char = None
            continue

        if marker:
            fence_char = marker[1][0]
            fence_length = len(marker[1])
            result.append(line)
            continue

        if FORMULA.fullmatch(line.rstrip("\r\n")):
            result.extend(["\n", line.rstrip("\r\n") + "\n", "\n"])
        else:
            result.append(line)

    return "".join(result)