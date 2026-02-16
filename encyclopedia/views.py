# from django.http import HttpResponse
from django.shortcuts import render, redirect
import markdown, random
from django.http import Http404
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
            "error_message": "404 The requested page was not found"
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
            "content": html_page,
            "title": entry_search
        })
        else:
            entries = util.list_entries()
            suggestions = []
            for entry in entries:   
                if entry_search.lower() in entry.lower():
                    suggestions.append(entry)
            return render(request, "encyclopedia/search-results.html", {
                "suggestions": suggestions,
                "entry_search": entry_search
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
                "error_message": "This entry already exists"
            })
        else:
            full_content = f"#{title}\n\n{content}"
            util.save_entry(title, full_content)
            html_page = md_conversion(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_page
            })
        
def edit_content(request, title):
    """
    Displays the form to edit an existing entry.
    This view should primarily handle GET requests.
    """
    
    if request.method != "GET":
        return redirect("index") 

    full_content = util.get_entry(title)
    
    if full_content is None:
        raise Http404("Entry does not exist.") 

        #Extract body content by stripping the H1 title ---
    body_content = ""
    lines = full_content.split('\n')
    
    if len(lines) > 0 and lines[0].startswith('#\w'):
        first_body_line_index = 1
        while first_body_line_index < len(lines) and not lines[first_body_line_index].strip():
            first_body_line_index += 1
        body_content = "\n".join(lines[first_body_line_index:])
    else:
        # Fallback if entry doesn't start with H1 (shouldn't happen if new_page works)
        body_content = full_content
        
        return render(request, "encyclopedia/edit-content.html", {
                "title": title,
                "content": body_content
            })
        
def save_changes(request):
    """
    Handles the POST request from the edit form to save changes.
    """
    if request.method == "POST":
        title = request.POST['title']        
        content = request.POST['content']    
        
        full_content = f"{content}"
        util.save_entry(title, full_content) 
        
        return redirect("entry_page", title=title)
    
    return redirect("index")

        
def random_page(request):
        entries = util.list_entries()
        random_entry = random.choice(entries)
        html_page = md_conversion(random_entry)
        return render(request, "encyclopedia/entry.html", {
             "title": random_entry,
             "content": html_page
        })