from pathlib import Path
from chameleon import PageTemplateLoader

templates_path = Path(__file__).resolve().parent / "templates"
template_loader = PageTemplateLoader(
    str(templates_path),
    ".html",
)

template = template_loader["index"]

leader="https://someimagename"
title = "this is a test"

item = dict()
item["mainphoto"] = "arz51qo1dtbyxmu1-640x853.jpg"
item["secondaryphoto"] = "arz51qo1dtbyxmu1-405x188.jpg"
item["title"] = "This is the title"

events = []
events.append(item)

with open("test.html", "w", encoding="utf-8") as text_file:
    text_file.write(template(leader="Banner-38-2023-600x750.jpg", title=title, events=events))
