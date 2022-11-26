from django.shortcuts import render
from markdown2 import Markdown
import random

from . import util


def md_to_html(title):
    content = util.get_entry(title)
    return None if content is None else Markdown().convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry(request, title):
    content = md_to_html(title)
    if content is None:
        return render(
            request,
            "encyclopedia/error.html",
            {"err_msg": "The page you are looking for does not exist."},
        )
    else:
        return render(
            request, "encyclopedia/entry.html", {"title": title, "content": content}
        )


def search(request):
    if request.method == "POST":
        search = request.POST["q"]
        content = md_to_html(search)
        if content is not None:
            return render(
                request,
                "encyclopedia/entry.html",
                {"title": search, "content": content},
            )
        else:
            entries = util.list_entries()
            recs = []
            for entry in entries:
                if search.lower() in entry.lower():
                    recs.append(entry)

            return render(
                request, "encyclopedia/search.html", {"recs": recs, "search": search}
            )


def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    elif request.method == "POST":
        title = request.POST["title"]
        page_content = request.POST["content"]
        exsisting_title = util.get_entry(title)

        if exsisting_title is not None:
            return render(
                request,
                "encyclopedia/error.html",
                {"err_msg": "The page you are trying to create already exists."},
            )
        else:
            util.save_entry(title, page_content)
            content = md_to_html(title)
            return render(
                request,
                "encyclopedia/entry.html",
                {"title": title, "content": content},
            )


def edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = util.get_entry(title)
        return render(
            request,
            "encyclopedia/edit.html",
            {"title": title, "content": content},
        )


def save(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        content = md_to_html(title)
        return render(
            request, "encyclopedia/entry.html", {"title": title, "content": content}
        )


def rand(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    content = md_to_html(random_entry)
    return render(
        request, "encyclopedia/entry.html", {"title": random_entry, "content": content}
    )
