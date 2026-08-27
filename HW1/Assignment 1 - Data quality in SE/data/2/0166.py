import jinja2
import markdown

from schema import (
    INDEX_FILES, INDEX_TITLE, INDEX_LINK,
    RESEARCH_FILES, RESEARCH_TITLE, RESEARCH_LINK,
    TEACHING_FILES, TEACHING_TITLE, TEACHING_LINK,
    PROGRAMMING_FILES, PROGRAMMING_TITLE, PROGRAMMING_LINK,
)


def convert_file(fname):
    """
    Convert markdown file `fname` to html. Returns html string.
    """
    md = markdown.Markdown(extensions=['extra'], tab_length=2)
    with open(fname, "r") as f:
        content = ''.join(f.readlines())
    return md.convert(content)


def make_page(source_md_files=[], pagename=None, pagetitle=""):
    if pagename is None:
        raise ValueError("pagename cannot be none")

    env = jinja2.Environment(loader=jinja2.loaders.FileSystemLoader('templates/'))
    template = env.get_template("page.html.jinja")

    content = []
    for sourcefile in source_md_files:
        fname = "markdown/" + sourcefile
        content.append(convert_file(fname))
    content_string = '\n'.join(content)

    with open(pagename, "w") as indexfile:
        indexfile.write(template.render(
                            title=pagetitle,
                            stuff=content_string,
                            link=pagename,
                        ))


def make_main_pages():
    make_page(
        source_md_files=INDEX_FILES,
        pagename="index.html",
        pagetitle=INDEX_TITLE,
    )
    make_page(
        source_md_files=RESEARCH_FILES,
        pagename="research.html",
        pagetitle=RESEARCH_TITLE,
    )
    make_page(
        source_md_files=TEACHING_FILES,
        pagename="teaching.html",
        pagetitle=TEACHING_TITLE,
    )
    make_page(
        source_md_files=PROGRAMMING_FILES,
        pagename="programming.html",
        pagetitle=PROGRAMMING_TITLE,
    )


def main():
    make_main_pages()


if __name__ == "__main__":
    main()
