# from django.http import HttpResponse
from django.shortcuts import render
import markdown, random


from . import util

"""
Function that converts md files to HTML using markdown library
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
    if request.method == 'POST':
        entry_search = request.POST['q']
        html_page = md_conversion(entry_search)
        if html_page is not None:
            return render(request, "encyclopedia/entry.html", {
            "title": entry_search,
            "content": html_page
        })
        else:
            entries = util.list_entries()
            suggestions = []
            for entry in entries:
                if entry_search.lower() in entry.lower():
                    suggestions.append(entry)
            return render(request, "encyclopedia/search-results.html", {
                "suggestions": suggestions
            })

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new-page.html", {
            "title": "Create a new page"
        })
    else: 
        title = request.POST['title']
        content = request.POST['content']
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html", {
                "error_message": "This page already exists"
            })
        else:
            util.save_entry(title, content)
            html_page = md_conversion(title)
            return render(request, "encyclopedia/entry.html", {
                title: title,
                "content": html_page
            })
        
def edit_content(request):
        if request.method == "POST":
            title = request.POST['title']
            content = util.get_entry(title)
            return render(request, "encyclopedia/edit-content.html", {
                "title": title,
                "content": content
            })
        
def save_changes(request):
        if request.method == "POST":
            title = request.POST['title']
            content = request.POST['content']
            util.save_entry(title, content)
            html_page = md_conversion(title)
            return render(request, "encyclopedia/entry.html", {
                    "title": title,
                    "content": html_page
                })
        
def random_page(request, title):
        entries = util.list_entries()
        random_entry = random.choice(entries)
        html_page = md_conversion(random_entry)
        return render(request, "encyclopedia/entry.html", {
             "title": random_entry,
             "content": html_page
        })
        

