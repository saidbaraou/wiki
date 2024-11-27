# from django.http import HttpResponse
from django.shortcuts import render
import markdown

from . import util

"""
Function that converts md files to HTML
"""
def md_conversion(title):
    md_page = util.get_entry(title)
    markdowner = markdown.Markdown()
    if md_page == None:
        return None
    else:
        return markdowner.convert(md_page)
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, title):
    if not title:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, f"encyclopedia/wiki/{title}", {
            "entry_page": util.get_entry(title)
        })