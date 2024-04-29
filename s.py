import webbrowser
website=input("search website: ")

if website=="google":
    name=input("search: ")
    webbrowser.open("https://www.google.com/search?q=" +name)
elif website=="youtube":
    name=input("search: ")
    webbrowser.open("https://www.youtube.com/watch?v=" +name)
elif website=="musescore":
    name=input("search: ")
    webbrowser.open("https://wynk.in/music/list/new-releases/amhyb_vnow19351643796144680?ref=" +name)
