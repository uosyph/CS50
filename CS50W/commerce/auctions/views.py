from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing, Comment, Bid


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def index(request):
    activeListing = Listing.objects.filter(isActive=True)
    allCats = Category.objects.all()
    return render(request, "auctions/index.html", {
        "listings": activeListing,
        "cats": allCats
    })


def create(request):
    if request.method == "GET":
        allCats = Category.objects.all()
        return render(request, "auctions/create.html", {
            "cats": allCats
        })
    elif request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["desc"]
        img = request.POST["img"]
        price = request.POST["price"]
        category = request.POST["category"]

        current_user = request.user

        cat_data = Category.objects.get(categoryName=category)

        bid = Bid(bid=float(price), user=current_user)
        bid.save()

        new_listing = Listing(
            title=title,
            desc=desc,
            img=img,
            price=bid,
            category=cat_data,
            owner=current_user
        )

        new_listing.save()

        return HttpResponseRedirect(reverse(index))


def showCat(request):
    if request.method == "POST":
        selectedCat = request.POST['category']
        category = Category.objects.get(categoryName=selectedCat)
        activeListing = Listing.objects.filter(
            isActive=True, category=category)
        allCats = Category.objects.all()
        return render(request, "auctions/index.html", {
            "listings": activeListing,
            "cats": allCats
        })


def listing(request, id):
    listingData = Listing.objects.get(pk=id)
    isInWatchlist = request.user in listingData.watchlist.all()
    comments = Comment.objects.filter(listing=listingData)
    isOwner = request.user.username == listingData.owner.username
    return render(request, "auctions/listing.html", {
        "listing": listingData,
        "isInWatchlist": isInWatchlist,
        "comments": comments,
        "isOwner": isOwner
    })


def addBid(request, id):
    newBid = request.POST['newBid']
    listingData = Listing.objects.get(pk=id)
    isInWatchlist = request.user in listingData.watchlist.all()
    comments = Comment.objects.filter(listing=listingData)
    isOwner = request.user.username == listingData.owner.username
    if float(newBid) > listingData.price.bid:
        updatedBid = Bid(user=request.user, bid=float(newBid))
        updatedBid.save()
        listingData.price = updatedBid
        listingData.save()
        return render(request, "auctions/listing.html", {
            "listing": listingData,
            "message": "Bid Updated Successfully",
            "updated": True,
            "isInWatchlist": isInWatchlist,
            "comments": comments,
            "isOwner": isOwner,
        })
    else:
        return render(request, "auctions/listing.html", {
            "listing": listingData,
            "message": "Bid Did not Update",
            "updated": False,
            "isInWatchlist": isInWatchlist,
            "comments": comments,
            "isOwner": isOwner,
        })


def endAuction(request, id):
    listingData = Listing.objects.get(pk=id)
    listingData.isActive = False
    listingData.save()
    isOwner = request.user.username == listingData.owner.username
    isInWatchlist = request.user in listingData.watchlist.all()
    comments = Comment.objects.filter(listing=listingData)
    return render(request, "auctions/listing.html", {
        "listing": listingData,
        "isInWatchlist": isInWatchlist,
        "comments": comments,
        "isOwner": isOwner,
        "updated": True,
        "message": "The Acution is Closed"
    })


def addToWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id,)))


def removeFromWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id,)))


def watchlist(request):
    currentUser = request.user
    listings = currentUser.watchlist.all()
    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })


def addComment(request, id):
    currentUser = request.user
    listingData = Listing.objects.get(pk=id)
    comment = request.POST['newComment']

    newComment = Comment(
        author=currentUser,
        listing=listingData,
        comment=comment
    )
    newComment.save()

    return HttpResponseRedirect(reverse("listing", args=(id,)))
