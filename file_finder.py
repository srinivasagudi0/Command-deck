def find_files(query):
    filename = query.replaceprefix("find ").strip()

    # will only search desktop, downloads and docs

    # get the whole ls of desktop
