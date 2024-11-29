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
    html_page = md_conversion(title)
    if html_page == None:
        return render(request, "encyclopedia/error.html", {
            "error_message": "The requested page was not found"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_page
        })

def search(request):
    return 